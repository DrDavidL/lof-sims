import json

import requests
import streamlit as st
from bs4 import BeautifulSoup
from fpdf import FPDF
from sqlalchemy import Column, Index, Integer, MetaData, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import markdown2
from sim_prompts import *  # Ensure this import provides the needed functionality

# Database setup
DATABASE_URL = "sqlite:///app_data.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define models
class Transcript(Base):
    __tablename__ = 'transcripts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    role = Column(String, nullable=False)
    specialty = Column(String, nullable=True)
    __table_args__ = (Index('transcript_content_idx', 'content'),)

class Assessment(Base):
    __tablename__ = 'assessments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    role = Column(String, nullable=False)
    specialty = Column(String, nullable=True)
    __table_args__ = (Index('assessment_content_idx', 'content'),)

class CaseDetails(Base):
    __tablename__ = 'case_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    saved_name = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    role = Column(String, nullable=False)
    specialty = Column(String, nullable=True)
    __table_args__ = (Index('case_details_content_idx', 'content'),)

Base.metadata.create_all(engine)

st.set_page_config(
    page_title='Simulated Case Generator',
    page_icon='🌌',
    layout="wide",
    initial_sidebar_state='auto'
)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, self.title, 0, 1, "C")
        self.ln(10)

    def chapter_title(self, title, level=1):
        self.set_font("Arial", "B", 16 if level == 1 else 14 if level == 2 else 12)
        self.ln(10 if level == 1 else 8 if level == 2 else 6)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_list(self, items, is_ordered=False):
        self.set_font("Arial", "", 12)
        for i, item in enumerate(items, start=1):
            self.multi_cell(0, 10, f"{i}. {item}" if is_ordered else f"- {item}")
        self.ln()

def html_to_pdf(html_content, name):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        case_title = soup.find("h1").get_text() if soup.find("h1") else "Document"
        pdf = PDF()
        pdf.title = case_title
        pdf.add_page()

        for element in soup.find_all(["h1", "h2", "h3", "p", "ul", "ol", "li", "hr"]):
            if element.name in ["h1", "h2", "h3"]:
                pdf.chapter_title(element.get_text(), level=int(element.name[1]))
            elif element.name == "p":
                pdf.chapter_body(element.get_text())
            elif element.name in ["ul", "ol"]:
                items = [li.get_text() for li in element.find_all("li")]
                pdf.add_list(items, is_ordered=(element.name == "ol"))
            elif element.name == "hr":
                pdf.add_page()
        
        pdf.output(name)
    except Exception as e:
        st.error(f"Error generating PDF: {e}")

def init_session():
    if "final_case" not in st.session_state:
        st.session_state["final_case"] = ""
    if "retrieved_case" not in st.session_state:
        st.session_state["retrieved_case"] = ""
    if "retrieved_name" not in st.session_state:
        st.session_state["retrieved_name"] = ""
    if "selected_case_id" not in st.session_state:
        st.session_state["selected_case_id"] = -1

def save_transcript(transcript_content, role, specialty):
    try:
        new_transcript = Transcript(content=transcript_content, role=role, specialty=specialty)
        session.add(new_transcript)
        session.commit()
    except Exception as e:
        st.error(f"Error saving transcript: {e}")

def save_assessment(assessment_content, role, specialty):
    try:
        new_assessment = Assessment(content=assessment_content, role=role, specialty=specialty)
        session.add(new_assessment)
        session.commit()
    except Exception as e:
        st.error(f"Error saving assessment: {e}")

def save_case_details(case_details_content, saved_name, role="", specialty=""):
    try:
        new_case_details = CaseDetails(content=case_details_content, saved_name=saved_name, role=role, specialty=specialty)
        session.add(new_case_details)
        session.commit()
    except Exception as e:
        st.error(f"Error saving case details: {e}")

def get_records(model, search_text=None, saved_name=None, role=None, specialty=None):
    try:
        query = session.query(model)
        if search_text:
            query = query.filter(model.content.ilike(f"%{search_text}%"))
        if saved_name:
            query = query.filter(model.saved_name.ilike(f"%{saved_name}%"))
        if role:
            query = query.filter_by(role=role)
        if specialty:
            query = query.filter_by(specialty=specialty)
        return query.all()
    except Exception as e:
        st.error(f"Error retrieving records: {e}")
        return []

def llm_call(model, messages):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {st.secrets['OPENROUTER_API_KEY']}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://fsm-gpt-med-ed.streamlit.app",
                "X-Title": "lof-sims",
            },
            data=json.dumps({"model": model, "messages": messages})
        )
        return response.json()
    except Exception as e:
        st.error(f"Error in LLM call: {e}")
        return {"choices": [{"message": {"content": "Error in LLM call."}}]}

def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.write("*Please contact David Liebovitz, MD if you need an updated password for access.*")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        return True

st.title("Case Study Framework Generator")
init_session()

if check_password():
    st.info("**Provide inputs and generate a case! Open the left sidebar to change models; default is inexpensive Haiku.**")

    with st.expander("Model Options for Case Generation (Claude3 Haiku by default)", expanded=False):
        model_choice = st.selectbox("Model Options", (
            "anthropic/claude-3-haiku",
            "anthropic/claude-3-sonnet", 
            "anthropic/claude-3-opus", 
            "openai/gpt-4-turbo", 
            "google/gemini-pro", 
            "meta-llama/llama-2-70b-chat",
        ), index=0)

    if "response_markdown" not in st.session_state:
        st.session_state["response_markdown"] = ""

    if "expanded" not in st.session_state:
        st.session_state["expanded"] = True

    if "edited_new_case" not in st.session_state:
        st.session_state["edited_new_case"] = ""
        
    roles = ["1st year medical student", "2nd year medical student", "3rd year medical student", "4th year medical student", "Resident", "Fellow", "Attending"]

    tab1, tab2 = st.tabs(["New Case", "Retrieve a Case"])

    with tab1:
        col1, col2, col3 = st.columns([1, 0.5, 4])

        with col1:    
            st.info("**Include desired history in the text paragraph. The AI will generate additional details as needed to draft an educational case.**")

            learning_objectives = st.multiselect(
                "Select one or more learning objectives; default is a focused history/examination",
                [
                    "Perform a focused history and examination",
                    "Provide patient education",
                    "Demonstrate effective interpersonal skills",
                    "Determine a Dx and DDx",
                    "Determine a plan for management",
                    "Document the patient case"
                ], default="Perform a focused history and examination",
                help="Choose the learning objectives relevant to this case study."
            )

            case_study_input = {
                'Case Title': st.text_input("Case Study Title"),
                'Case Description': st.text_area("Case Study Description, as detailed or brief as desired, e.g., 65F with acute chest pain...", height=200),
                'Case Primary Diagnosis': st.text_input("Case Primary Diagnosis, e.g., Pulmonary Embolism"),
            }
            case_study_input = json.dumps(case_study_input)

            st.info("Click submit when ready to generate a case! A download button will appear in the next column once generated.")
            submit_button = st.button("Submit")

        if submit_button:
            messages = [
                {"role": "system", "content": 'Use input provided with additional AI generated content to fully flesh out a clinical case optimized for simulation using the following format: {output_format}'},
                {"role": "user", "content": f'case_details: {case_study_input}, learning_objectives: {learning_objectives}'}
            ]

            with col2:
                with st.spinner("Assembling Case... Please wait."):
                    response_content = llm_call(model_choice, messages)
            st.session_state.response_markdown = response_content['choices'][0]['message']['content']

        if st.session_state.response_markdown:
            with col3:
                st.success("Case Study Framework Generated!")
                with st.expander("View Full Case", expanded=st.session_state.expanded):
                    st.markdown(st.session_state.response_markdown)
                    st.session_state.expanded = False

                st.info("Review and/or edit the case and begin the simulator!")                  
                if st.checkbox("Edit Case (Scroll Down)", value=False):
                    with col3:
                        st.session_state.expanded = False
                        st.warning("Please edit the case as needed while leaving other characters, e.g., '#' and '*', in place. Use the 'Save Case Edits' button at the bottom to save edits!")
                        edited_new_case = st.text_area("Click button at bottom to save your edits!", st.session_state.response_markdown, height=1000) 
                        if st.button("Save Case Edits for the Simulator"):
                            st.success("Case Edits Saved!")
                            if edited_new_case:
                                st.session_state["final_case"] = edited_new_case
                        st.page_link("pages/🧠_Sim_Chat.py", label="Click Here to Wake the Simulator (including any saved edits)", icon="🧠")
                else:
                    st.session_state["final_case"] = st.session_state.response_markdown
                
                if st.session_state.final_case:
                    case_html = markdown2.markdown(st.session_state.final_case, extras=["tables"])
                    if st.checkbox("Generate Case PDF file"):
                        html_to_pdf(case_html, 'case.pdf')
                        with open("case.pdf", "rb") as f:
                            st.download_button("Download Case PDF", f, "case.pdf")

                    if st.button("Send case to the simulator!"):
                        st.session_state["final_case"] = st.session_state.final_case
                        st.session_state["retrieved_name"] = st.session_state.retrieved_name
                        st.page_link("pages/🧠_Sim_Chat.py", label="Click Here to Wake the Simulator", icon="🧠")

            
            if st.session_state.final_case:
                st.divider()
                st.header("Save Case to the Database for Future Use, too!")
                case_details = st.text_area("Case Details to Save to the Database for Future Use", value=st.session_state.final_case)
                saved_name = st.text_input("Saved Name (Required to save case)")

                if st.button("Save Case to the Database for future use!"):
                    if saved_name:
                        save_case_details(case_details, saved_name)
                        st.success("Case Details saved successfully!")
                    else:
                        st.error("Saved Name is required to save the case")

    if "search_results" not in st.session_state:
        st.session_state.search_results = []
    if "selected_case" not in st.session_state:
        st.session_state.selected_case = None

    with tab2:
        st.header("Retrieve Records")
        search_text = st.text_input("Search Text")
        search_saved_name = st.text_input("Search by Saved Name")
        search_role = st.selectbox("Search by Role", [""] + roles)
        search_specialty = st.text_input("Search by Specialty", "") if search_role in ["Resident", "Fellow", "Attending"] else ""

        if st.button("Search Cases"):
            st.session_state.search_results = get_records(CaseDetails, search_text, search_saved_name, search_role, search_specialty)

        if st.session_state.search_results:
            st.subheader("Cases Found")
            for i, case in enumerate(st.session_state.search_results):
                st.write(f"Saved Name: {case.saved_name}, Role: {case.role}, Specialty: {case.specialty}")
                if st.button(f"View (and Select) Case {i+1}", key=f"select_case_{i}"):
                    st.session_state.selected_case = case

        if st.session_state.selected_case:
            st.subheader("Retrieved Case")
            with st.expander("View Full Case", expanded=False):
                st.write(f'Here is the retrieved case name: {st.session_state.selected_case.saved_name}')
                st.write(st.session_state.selected_case.content)
                st.session_state.final_case = st.session_state.selected_case.content
            if st.checkbox("Edit Case (Scroll Down)", value=False, key="initial_case_edit"):
                st.session_state.expanded = False
                st.warning('Please edit the case as needed while leaving other characters, e.g., "#" and "*", in place. Remember to update the Door Chart section at the bottom!')
                updated_retrieved_case = st.text_area("Edit Case, enter control-enter or command-enter to save edits!", st.session_state.selected_case.content, height=1000)
                make_new_entry = st.checkbox("Make a new entry with the edited case", value=False)
                if make_new_entry:
                    saved_name = st.text_input("Saved Name after edits (Required to save case)")
                if st.button("Save Edits"):
                    st.session_state.final_case = updated_retrieved_case
                    st.info("Case Edits Saved!")
                    if make_new_entry and saved_name:
                        save_case_details(updated_retrieved_case, saved_name)
                        st.success("Case Details saved successfully!")
                    elif make_new_entry and not saved_name:
                        st.error("Saved Name is required to save the case")

            st.page_link("pages/🧠_Sim_Chat.py", label="Click Here to Wake the Simulator", icon="🧠")

