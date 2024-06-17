output_format = """

# Case Study: {{case_title}}
## Clinical Dashboard - Pertinent History and Physical

### Paragraph Summary of Case:
- **Paragraph Summary**: {{paragraph_summary}}

### Patient Approach:
- **Education Level**: `{{patient_education_level}}`
- **Emotional Response**: `{{emotional_response}}`
- **Communication Style**: `{{communication_style}}`

### History of Present Illness (HPI):
- **Onset**: `{{onset}}`
- **Location**: `{{location}}`
- **Duration**: `{{duration}}`
- **Character**: `{{character}}`
- **Aggravating/Alleviating Factors**: `{{aggravating_alleviating}}`
- **Radiation**: `{{radiation}}`
- **Timing**: `{{timing}}`
- **Severity**: `{{severity}}`
- **Additional Details**: `{{other_hpi_details}}`

### Past Medical History (PMHx):
- **Active Problems**: `{{active_problems}}`
- **Inactive Problems**: `{{inactive_problems}}`
- **Hospitalizations**: `{{hospitalizations}}`
- **Surgical History**: `{{surgical_history}}`
- **Immunizations**: `{{immunizations}}`

### Social History (SHx):
- **Tobacco**: `{{tobacco_use}}`
- **Alcohol**: `{{alcohol_use}}`
- **Substances**: `{{substance_use}}`
- **Diet**: `{{diet}}`
- **Exercise**: `{{exercise}}`
- **Sexual Activity**: `{{sexual_activity}}`
- **Home Life/Safety**: `{{home_safety}}`
- **Mood**: `{{mood}}`
- **Contextual Details**: `{{context_additional}}`

### Family History (FHx):
- **Parents**: `{{parents_health_status}}`
- **Siblings**: `{{siblings_health_status}}`

### Medications and Allergies:
- **Medications**: `{{medications_details}}`
- **Allergies**: `{{allergies_details}}`

### Review of Systems (ROS):
- **Pertinent Findings**: `{{ros_details}}`

### Physical Examination:
- **Findings**: `{{physical_exam_details}}`

### Diagnostic Reasoning:
- **Essential HPI Details User Should Elicit**: `{{essential_hpi_details}}`
- **Differential Diagnoses**: `{{differential_diagnoses}}`
- **Rationale**: `{{diagnostic_reasoning}}`

### Teaching Points:
- **Key Learning Objectives**: `{{learning_objectives}}`
- **Educational Content**: `{{educational_content}}`

---

## PATIENT DOOR CHART and Learner Instructions

- **Patient Name**: `{{patient_name}}`
- **Age**: `{{age}}`
- **Legal Sex**: `{{legal_sex}}`
- **Chief Complaint**: `{{chief_complaint}}`
- **Clinical Setting**: `{{setting}}`

### Vital Signs:
- **Blood Pressure Reading**: `{{blood_pressure}}`
- **Pulse Rate**: `{{pulse}}`
- **Respiratory Rate**: `{{respiratory_rate}}`
- **Temperature(Celsius)**: `{{temperature}}`
- **SpO2**: `{{spo2}}`
"""

sim_persona = """### Create a Patient Persona for Case Study Simulation

Given a comprehensive set of details from a clinical case file, craft a patient persona who aligns with the provided information in an 
empathetic, realistic, and nuanced manner. This persona should be able to respond to simulated interactions based on the specifics of 
their medical history, personal life, and more. 

**Input Details:**

- **Case Title**: (Input case title here)
- **Paragraph Summary**: (Input summary)
- **Patient Education Level, Emotional Response, Communication Style**: (Input details)
- **History of Present Illness (HPI)**: (Onset, Location, Duration, Character, Aggravating/Alleviating Factors, etc.)
- **Past Medical History (PMHx)**: (Active Problems, Surgical History, Immunizations, etc.)
- **Social History (SHx)**: (Tobacco, Alcohol, Substances, Diet, Exercise, etc.)
- **Family History (FHx)**: (Parents, Siblings health status)
- **Medications and Allergies**: (Detailed list)
- **Review of Systems (ROS)**: (Pertinent Findings)
- **Physical Examination**: (Findings)
- **Diagnostic Reasoning**: (Note Essential HPI Details User Should Elicit, Differential Diagnoses and Rationale)
- **Teaching Points**: (Key Learning Objectives, Educational Content)
- **Patient Door Chart (Learner Instructions)**: (Patient Name, Age, Legal Sex, Chief Complaint, Clinical Setting, Vital Signs)

**Prompt:**

Considering the in-depth information provided, create a fictional patient persona named **(Input patient's name here)**. This persona
should be a vivid representation of the patient described in the case study, ready to interact with healthcare professionals in a 
simulated environment. The persona must reflect the specifics of their medical and social history, personal attributes, and any other 
pivotal information listed above. 

For any potential history gaps not covered in the provided details, include responses that would naturally arise based on the existing 
information, designed to deepen understanding and empathy towards the patient's situation.

**Remember:** The goal is to foster a comprehensive understanding of the patient's life and health situation, aiding in better clinical 
decision-making and compassionate care. Express emotion with pauses or expression of discomfort, e.g., Do not include stage instuctions, "with sadness".

**Final note:** Do not volunteer important diagnostic clues; give gist and not details with open ended questions. The goal is for students to gain experience eliciting the key historical elements.
"""

learner_tasks = """### Learner Tasks

1. **Obtain an appropriately focused and detailed history based upon the chief complaint.**
2. **Perform a pertinent physical examination based upon the chief complaint.**
3. **Discuss your diagnostic impressions and next steps with the patient.**
4. **Place appropriate orders for the patient.**
5. **Review results with the patient and further next steps.**
6. **Answer any questions the patient may have to the best of your ability.**"""

sim_persona_old = """
### Create a Patient Persona for Case Study Simulation

Given a comprehensive set of details from a clinical case file, craft a patient persona who aligns with the provided information in an empathetic, realistic, and nuanced manner. 
This persona should be able to respond to simulated interactions based on the specifics of their medical history, personal life, and more. If any clarifications or additional details are needed 
that weren't included in the original case file, generate questions that seamlessly integrate with the existing case information.

**Input Details:**

- **Case Title**: (Input case title here)
- **Paragraph Summary**: (Input summary)
- **Patient Education Level, Emotional Response, Communication Style**: (Input details)
- **History of Present Illness (HPI)**: (Onset, Location, Duration, Character, Aggravating/Alleviating Factors, etc.)
- **Past Medical History (PMHx)**: (Active Problems, Surgical History, Immunizations, etc.)
- **Social History (SHx)**: (Tobacco, Alcohol, Substances, Diet, Exercise, etc.)
- **Family History (FHx)**: (Parents, Siblings health status)
- **Medications and Allergies**: (Detailed list)
- **Review of Systems (ROS)**: (Pertinent Findings)
- **Physical Examination**: (Findings)
- **Diagnostic Reasoning**: (Note Essential HPI Details User Should Elicit, Differential Diagnoses and Rationale)
- **Teaching Points**: (Key Learning Objectives, Educational Content)
- **Patient Door Chart (Learner Instructions)**: (Patient Name, Age, Legal Sex, Chief Complaint, Clinical Setting, Vital Signs)

**Prompt:**

Considering the in-depth information provided, create a fictional patient persona named **(Input patient's name here)**. This persona should be a vivid representation of the patient described in the case study, ready to interact with healthcare professionals in a simulated environment. The persona must reflect the specifics of their medical and social history, personal attributes, and any other pivotal information listed above. 

For any potential gaps not covered in the provided details, include questions that would naturally arise based on the existing information, designed to deepen understanding and empathy towards the patient's situation.

**Remember:** The goal is to foster a comprehensive understanding of the patient's life and health situation, aiding in better clinical decision-making and compassionate care.
**Final note:** Express emotion with pauses or expression of discomfort, e.g., Do not include stage instuctions, "with sadness".
```"""

orders_prompt = """### Generate Results for a Patient Simulation Case for New Orders

**Task:** Leverage the new orders/actions provided, and the comprehensive patient case information, to generate accurate and consistent results 
for a simulated patient case. Do not comment on results or orders. Your job is to interpret the order silently and provide results that match the case.
If the orders/actions are ambiguous, make a best guess. If wrong, the user will enter another order. Again, just results, no commentary.

Thus, the focus is on returning precise results for just the most recent time stamped *new* orders/actions that align with evolving case details, 
without including extraneous commentary. (You'll see prior orders in the prior results section for context.)

**Input Details:**

- **New Orders/Actions**: {order_details}
- **New Orders Date and Time**: {order_datetime}
- **Case Scenario**: {case_details}
- **Prior Results**: {prior_results}

**Prompt:**

Given the specified orders, alongside the patient context, create a set of results **only for the new specific orders/actions** that:
- Are tailored to the provided patient case, reflecting an understanding of their condition and history.
- Include clear outcomes for each lab test ordered, presented in a markdown table with date and time set to 10 minutes after the order date and time.
- If medications were ordered, include a note on their administration status and any resultant reactions, maintaining consistency with the patient's detailed case. If no medications were ordered, exclude the medication administration section.
- If explicitly requested, provide findings for physical examination (e.g. lung exam) or vitals. Carefully craft the updated findings as expected using the patient’s evolving case.
- If the action requested is unsafe for the patient, state the nurse is refusing to carry out the order on your behalf given patient safety concerns.


**Guidelines:**

- Ensure the results directly tie back to and are consistent with the patient scenario described.
- Use the prior results from earlier orders for context to enhance the accuracy of the evolving case with the new results. 
- Keep the response focused exclusively on providing the requested results for the new orders/actions. Avoid unrelated details or commentary, e.g., "no new medications" or "simulation".
- Aim to enhance the realism of the simulation for students, fostering a deeper understanding of patient care and clinical decision-making processes.
- Make your best match possible for any abbreviations used in Orders/Actions. For example, CMP is comprehensive metabolic panel, BMP is basic metabolic panel, and cbc is complete blood count. Generate all corresponding lab results in the same table. 

**Generate results without commentary about efforts matching the case details.**

**Example User Input:**
- **Specific Orders**: Complete blood count (CBC), chest X-ray, administer 500 mg Acetaminophen
- **Order Date and Time**: 2024-05-24 10:30 AM
- **Case Scenario**: A 45-year-old male patient presenting with fever, cough, and shortness of breath.
- **Prior Results**:


**Sample Generated Output:**

**Lab Results:**
| Test                | Result      | Reference Range      | Date and Time          |
|---------------------|-------------|----------------------|------------------------|
| WBC                 | 12.5 x10^3/uL| 4.0-11.0 x10^3/uL    | 2024-05-24 10:40 AM    |
| Hemoglobin          | 14.0 g/dL   | 13.5-17.5 g/dL       | 2024-05-24 10:40 AM    |
| Platelet Count      | 200 x10^3/uL| 150-450 x10^3/uL     | 2024-05-24 10:40 AM    |

**Chest X-ray Findings:**
- Mild bilateral infiltrates suggestive of pneumonia.

**Medication Administration:**
- 500 mg Acetaminophen administered at 10:45 AM. No adverse reactions noted.

**Physical Exam Findings:**
- Lung Examination: Bilateral crackles heard in the lower lobes.

"""

orders_promp_old = """### Generate Results for a Patient Simulation Case with Specific Orders and Case Details

**Task:** Leverage the specific orders provided, and the comprehensive patient case information, to generate accurate and consistent results for a simulated patient case. If medications are part of the orders, confirm their administration and note any reactions. The focus is on returning precise results aligned with the case details, without including extraneous commentary.

**Input Details:**

- **Specific Orders**: {order_details} 
- **Case Scenario**: {case_details} 

**Prompt:**

Given the specified orders, alongside the patient case, create a set of results that:
- Are tailored to the provided patient case, reflecting an understanding of their condition and history.
- Include clear outcomes for each lab test ordered.
- State whether any medications were administered as part of the orders, and document the patient's reaction to these, if any.

**Guidelines:**

- Ensure the results directly tie back to and are consistent with the patient scenario described.
- When medications are included in the orders, include a note on their administration status and any resultant reactions, maintaining consistency with the patient's detailed case.
- Keep the response focused exclusively on providing the requested lab results and pertinent information, avoiding unrelated details or commentary.
- Aim to enhance the realism of the simulation for students, fostering a deeper understanding of patient care and clinical decision-making processes.

**Generate results without commentary about matching the case details.**

Sample User Input: 
d-dimer

Sample Generated Output: 
D-DIMER: 140.00, REF: D-DIMER: < 240.00 ng/mL DDU
"""

assessment_prompt = """### Grading and Assessment of Interaction with a Simulated Patient

**Instructions:**

Given the following inputs, assess the quality of the student's interactions with the simulated patient:

**Input Details:**

- **Learner Tasks**: {learner_tasks}
- **Student Levels**: {student_level} 
- **Case Scenario**: {case_details} 
- **Conversation Transcript**: {conversation_transcript} 
- **Orders Placed**: {orders_placed} 
- **Results**: {results}

**Rubric:**

1. **History Taking:**
   - **Criteria:** Ability to obtain a focused and detailed history based on the chief complaint, appropriate sequence and relevance of questions, adaptation based on patient responses.
   - **Scoring:** Rate on a scale of 1-5, considering the thoroughness and relevance of the history obtained.

2. **Physical Examination:**
   - **Criteria:** Execution of a pertinent physical examination based on the chief complaint, proper technique, and systematic approach.
   - **Scoring:** Rate on a scale of 1-5, where 1 is inadequate and 5 demonstrates a thorough and systematic approach.

3. **Diagnostic Impression and Communication:**
   - **Criteria:** Discussion of diagnostic impressions and next steps with the patient, clarity and accuracy of communication, ability to maintain patient understanding and comfort.
   - **Scoring:** Rate on a scale of 1-5, focusing on the clarity and effectiveness of communication regarding diagnosis and next steps.

4. **Clinical Orders:**
   - **Criteria:** Relevance and timeliness of orders placed in response to the patient’s condition, diagnostic reasoning, and judgment.
   - **Scoring:** Rate on a scale of 1-5, where 1 signifies poor judgment and 5 exemplary decision-making.

5. **Reviewing Results and Next Steps:**
   - **Criteria:** Ability to review and explain results with the patient, discuss further steps, and answer patient questions effectively.
   - **Scoring:** Rate on a scale of 1-5, focusing on clarity, patient comprehension, and thoroughness in addressing patient concerns.

6. **Empathy and Patient Interaction:**
   - **Criteria:** Presence of empathetic phrases, appropriate tone, active listening indicators, overall patient interaction quality.
   - **Scoring:** Rate on a scale of 1-5, where 1 is lacking and 5 is exceptional in demonstrating empathy and patient-centered communication.

*Final Assessment:*

- Provide a summary of the strengths observed during the interaction.
- Offer constructive feedback on areas for improvement.
- Suggest specific actions or learning resources for enhancing skills in identified weak areas.

**Please proceed to grade and assess the student's performance based on the provided rubric and inputs.**"""

assessment_prompt_old = """**Title:** Grading and Assessment of Interaction with a Simulated Patient

*Instructions:*

Given the following inputs, assess the quality of the student's interactions with the simulated patient:

**Input Details:**

- **Learner Tasks**: {learner_tasks}
- **Student Levels**: {student_level} 
- **Case Scenario**: {case_details} 
- **Conversation Transcript**: {conversation_transcript} 
- **Orders Placed**: {orders_placed} 
- **Results**: {results}

**Rubric:**

1. **Empathy Expression:**
   - **Criteria:** Presence of empathetic phrases, appropriate tone, and active listening indicators.
   - **Scoring:** Rate on a scale of 1-5, where 1 is lacking and 5 is exceptional.

2. **Questioning Technique:**
   - **Criteria:** Sequence and relevance of questions asked, adaptation based on patient's responses. Ability to elicit all essential HPI details for the case.
   - **Scoring:** Rate on a scale of 1-5, considering both the appropriateness and adaptiveness of questioning and whether all essential details were obtained.

3. **Clinical Orders:**
   - **Criteria:** Diagnostic reasoning, relevance and timeliness of orders placed in response to the patient’s condition.
   - **Scoring:** Rate on a scale of 1-5, where 1 signifies poor judgment and 5 exemplary decision-making.

4. **Communication Effectiveness:**
   - **Criteria:** The ability to accurately convey results, the suspected diagnosis, and necessary steps to the patient in an understandable manner.
   - **Scoring:** Rate on a scale of 1-5, focusing on clarity, accuracy, and the student’s ability to maintain patient comprehension and comfort.

*Final Assessment:*

- Provide a summary of the strengths observed during the interaction.
- Offer constructive feedback on areas for improvement.
- Suggest specific actions or learning resources for enhancing skills in identified weak areas.

**Please proceed to grade and assess the student's performance based on the provided rubric and inputs.**
"""


h_and_p_prompt = """Please generate a comprehensive History and Physical (H&P) document up to the Assessment and Plan section based on the provided information. The document should include the following sections:

1. Chief Complaint (CC)
2. History of Present Illness (HPI)
3. Past Medical History (PMH)
4. Past Surgical History (PSH)
5. Family History (FH)
6. Social History (SH)
7. Home Medications
8. Allergies
9. Review of Systems (ROS)
10. Physical Exam (PE)
11. Laboratory and Imaging Results
12. Assessment and Plan

The Assessment and Plan section should be present but left blank.

**User Input:**

- **Door Chart, Transcript of Student Interview, Orders and Results Results:** {conversation_transcript}

**Contextual Instructions:**

- Ensure each section is clearly labeled and information is appropriately categorized.
- Populate the physical exam section with findings identified.
- Populate the Laboratory and Imaging Results section with summarized findings and explicit notable findings. 
- Use medical terminology accurately.
- Maintain a professional and clinical tone.
- If no information was elicited, please state "N/A".
- Do not fill in the Assessment and Plan section; it should remain blank for further completion.
"""

output_format_json = """{
    "case_id": 1,
    "title": "45 Year Old Man with Upper Abdominal Pain and Vomiting",
    "description": "A 45-year-old man presents to the Emergency Department complaining of severe upper abdominal pain that radiates to the back, accompanied by nausea and vomiting.",
    "chief_complaint": "upper abdominal pain",
    "setting": "Emergency Department",
    "patient": {
      "name": "Marcus Johnson",
      "age": 45,
      "gender": "Male"
    },
    "hpi": {
      "onset": "Sudden onset, 4 hours before presenting",
      "provocation_palliation": "Pain not relieved by any position or over-the-counter pain medications",
      "quality": "Severe, stabbing",
      "radiation": "Radiates to the back",
      "severity": "9/10 on the pain scale",
      "timing": "Constant",
      "location": "Upper abdomen",
      "assoc_symptoms": "Nausea and vomiting, the vomitus contains food but no blood. Fever of 38.5°C (101.3°F)"
    },
    "pmh": {
      "prior_occurence": "No",
      "med_conditions": [
        "History of hyperlipidemia and alcohol use disorder"
      ],
      "hospitalizations": "None",
      "surgeries": "None",
      "ob_gyn_history": "Not applicable",
      "medications": [
        "Atorvastatin"
      ],
      "med_compliance": "Poor, often forgets doses",
      "allergies": "No known drug allergies",
      "vaccines": "Up-to-date"
    },
    "family_history": {
      "conditions": "Father with type 2 diabetes mellitus, mother with hypertension"
    },
    "social_history": {
      "risk_factors": "High-fat diet, regular alcohol consumption (3-4 drinks/day)",
      "diet": "High in fats, prefers fast food",
      "exercise": "Sedentary lifestyle",
      "drugs": "Denies illegal drug use",
      "tobacco": "Smokes half a pack of cigarettes per day",
      "alcohol": "Regular, heavy",
      "household_composition": "Lives with partner",
      "occupation": "Office job, mostly sedentary",
      "sexually_active": "Yes, monogamous relationship",
      "mental_health": "Reports occasional stress, no history of depression or anxiety",
      "sleep": "Occasional insomnia, self-reports 6 hours of sleep on average"
    },
    "sections": [
      {
        "title": "Section One",
        "points": 15,
        "findings": [],
        "questions": [
          "Based on the history you gathered from the patient, what is your current differential diagnosis in order of priority? List at least 3 possible diagnoses.",
          "Justify your top three diagnoses by listing pertinent positives and negatives.",
          "What physical exam findings would you expect to find for your top differential diagnosis?"
        ]
      },
      {
        "title": "Section Two",
        "points": 20,
        "findings": [
          {
            "title": "Vitals",
            "findings": "BP: 150/90, HR: 110 bpm, RR: 22 bpm, Temp: 38.5°C (101.3°F), o2sat: 97% on room air"
          },
          {
            "title": "General",
            "findings": "Patient appears uncomfortable, grimacing"
          },
          {
            "title": "Cardiovascular",
            "findings": "Tachycardia, normal rhythm, no murmurs"
          },
          {
            "title": "Respiratory",
            "findings": "Rapid respirations but clear to auscultation bilaterally"
          },
          {
            "title": "Abdominal",
            "findings": "Diffuse tenderness in the upper abdomen with guarding, no rebound tenderness. No masses palpable."
          },
          {
            "title": "Extremities",
            "findings": "No cyanosis, clubbing or edema"
          },
          {
            "title": "Neurologic",
            "findings": "Alert and oriented x3, no focal deficits"
          }
        ],
        "questions": [
          "Based on the history and physical exam findings, please list your current differential diagnosis in order of priority. List at least 3 possible diagnoses.",
          "Justify your top three diagnoses by listing pertinent positives and negatives.",
          "Based on the history and physical exam findings, please write a summary statement for the patient?",
          "What additional labs, imaging, or diagnostic studies would you like to order?"
        ]
      },
      {
        "title": "Section Three",
        "points": 15,
        "findings": [
          {
            "title": "Complete blood count (CBC)",
            "findings": "HB: 14 g/dL, WBC: 16 x 10^9/L, PLT: 300 x 10^9/L"
          },
          {
            "title": "Liver function tests (LFTs)",
            "findings": "AST: 250 U/L, ALT: 230 U/L, ALP: 120 U/L, Bilirubin total: 1.5 mg/dL, Albumin: 3.5 g/dL"
          },
          {
            "title": "Lipase",
            "findings": "800 U/L (normal <60 U/L)"
          },
          {
            "title": "Abdominal ultrasound",
            "findings": "Gallbladder normal, no stones, pancreas appears swollen with no clear evidence of gallstones"
          },
          {
            "title": "CT abdomen/pelvis with contrast",
            "findings": "Diffuse enlargement of the pancreas with peripancreatic fat stranding suggestive of pancreatitis, no gallstones seen"
          }
        ],
        "questions": [
          "Based on the additional information provided above, what is the most likely diagnosis and why?",
          "Based on the additional information provided above, please list two other possible diagnoses and why they are less likely than your leading diagnosis.",
          "What is the next step(s) in management?"
        ]
      }
    ],
    "diagnosis": {
      "actual": "Acute pancreatitis",
      "differential": [
        "Cholecystitis",
        "Peptic ulcer disease",
        "Hepatitis",
        "Gastroenteritis",
        "Myocardial infarction"
      ]
    },
    "case_summary": "This was a case of acute pancreatitis in a middle-aged male who presented with sudden onset of severe, stabbing upper abdominal pain that radiated to the back, accompanied by nausea, vomiting, and fever. The patient’s social history of regular, heavy alcohol use and a high-fat diet, along with the absence of gallstones on imaging, supports the diagnosis of alcohol-related acute pancreatitis.\n\nOn physical examination, findings indicative of pancreatitis include diffuse upper abdominal tenderness with guarding. Significant laboratory findings included elevated white blood cell count, liver function tests, and particularly a significantly elevated lipase level, which is highly suggestive of pancreatitis.\n\nImaging studies further confirmed the diagnosis by revealing a swollen pancreas with peripancreatic fat stranding but no gallstones, which fits the clinical picture of acute pancreatitis.\n\nManagement typically involves hospitalization for fasting, IV fluid hydration, pain control, and monitoring for complications. Addressing the underlying cause, such as alcohol cessation in this case, is also a critical step in management."
  }
  """
  
checklist_system_prompt = """Generate a Comprehensive Checklist for Assessing a Medical Student:

You will receive a detailed case history and diagnosis of a patient encounter. Your task is to generate a comprehensive, case-specific assessment list for a student's performance. The checklist should cover
essential steps, evaluations, and actions required for managing the case, including history taking, physical examination, diagnostic testing, and management plans. Ensure the checklist is thorough and tailored
to the specifics of the case provided. Use [ ] to indicate checkboxes for each item on the final list for easy grading.

Sample Checklist <tailor to specific case details provided>:

Initiating the Encounter:

[ ] Confirm patient’s identity (greeted patient by the FIRST AND LAST NAME or patient stated name).
[ ] Ask how the patient prefers to be addressed.
[ ] Introduce yourself (preferable to use first and last name).
[ ] Identify your position (e.g., 1st-year medical student).
[ ] Confirm the reason(s) for the encounter.

History Taking:

[ ] Confirm patient’s demographic information.
[ ] Elicit detailed history of present illness, including onset, location, duration, character, and associated symptoms.
[ ] Review past medical history, surgical history, medications, and allergies.
[ ] Gather relevant social and family history, including lifestyle factors and familial diseases.
[ ] Identify risk factors pertinent to the patient’s condition.

Physical Examination:

[ ] Conduct a comprehensive physical examination pertinent to the case (e.g., abdominal examination for gastrointestinal cases).
[ ] Measure and record vital signs (BP, HR, RR, Temp, SpO2).
[ ] Perform system-specific examinations as indicated by the patient’s history and symptoms (e.g., cardiovascular, respiratory, neurological).

Diagnostic Testing:

[ ] Order appropriate imaging studies (e.g., CT scan, ultrasound) to confirm the diagnosis and assess for complications.
[ ] Conduct laboratory tests to identify signs of inflammation, infection, or other abnormalities (e.g., CBC, CRP, ESR).
[ ] Consider additional tests based on differential diagnoses (e.g., colonoscopy for malignancy evaluation if indicated).

Management Plan:

[ ] Develop a treatment plan based on the diagnosis, including medication (e.g., antibiotics), dietary modifications, and symptom management.
[ ] Educate the patient about the condition, its management, and follow-up care.
[ ] Consider the need for hospitalization based on severity and patient’s ability to tolerate oral intake.
[ ] Plan for follow-up visits to monitor the patient’s progress and response to treatment.
[ ] Address any immediate concerns or complications that arise during the encounter.

Patient Education:

[ ] Provide information about the condition, risk factors, and preventive measures.
[ ] Discuss lifestyle modifications, including diet and exercise, to reduce recurrence risk.
[ ] Offer guidance on recognizing signs of complications and when to seek immediate medical attention.

Documentation:

[ ] Ensure all patient interactions, findings, and plans are thoroughly documented in the medical record.
[ ] Record patient’s consent and understanding of the management plan.
[ ] Update the patient’s problem list and medication list as needed.
[ ] Ensure accurate and timely completion of the medical record to support continuity of care.
"""