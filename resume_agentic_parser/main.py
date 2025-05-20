import os
import pandas as pd
from tqdm import tqdm

from agents.text_extractor import TextExtractorAgent
from agents.name_agent import NameAgent
from agents.contact_agent import ContactAgent
from agents.education_agent import EducationAgent
from agents.experience_agent import ExperienceAgent
from agents.skills_agent import SkillsAgent

# Initialize agents
text_agent = TextExtractorAgent()
name_agent = NameAgent()
contact_agent = ContactAgent()
education_agent = EducationAgent()
experience_agent = ExperienceAgent()
skills_agent = SkillsAgent()

resume_folder = "resumes"
output_excel = "parsed_resume_data.xlsx"
data_rows = []

# Ensure resumes folder exists
if not os.path.exists(resume_folder):
    os.makedirs(resume_folder)

# Process resumes
for filename in tqdm(os.listdir(resume_folder)):
    if filename.lower().endswith(".pdf"):
        path = os.path.join(resume_folder, filename)
        try:
            text = text_agent.run(path)
            name = name_agent.run(text)
            contact = contact_agent.run(text)
            education = education_agent.run(text)
            experience = experience_agent.run(text)
            skills = skills_agent.run(text)

            data_rows.append({
                "File Name": filename,
                "Full Name": name,
                "Email": contact["Email"],
                "Phone": contact["Phone"],
                "Education": education,
                "Work Experience": experience,
                "Skills": skills
            })
        except Exception as e:
            data_rows.append({
                "File Name": filename,
                "Full Name": "Error",
                "Email": f"Error: {str(e)}",
                "Phone": "",
                "Education": "",
                "Work Experience": "",
                "Skills": ""
            })

# Export to Excel
df = pd.DataFrame(data_rows)
df.to_excel(output_excel, index=False)
print(f"\n✅ Done! Extracted data written to {output_excel}")
