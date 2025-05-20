class ExperienceAgent:
    def run(self, text):
        keywords = ["experience", "developer", "engineer", "intern", "worked", "company", "project", "manager"]
        return "; ".join([line.strip() for line in text.split("\n") if any(k.lower() in line.lower() for k in keywords)])
