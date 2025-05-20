class SkillsAgent:
    def run(self, text):
        skills_list = ["Python", "Java", "C++", "SQL", "JavaScript", "Django", "React", "Machine Learning", "Git", "AWS"]
        return ", ".join([skill for skill in skills_list if skill.lower() in text.lower()])
