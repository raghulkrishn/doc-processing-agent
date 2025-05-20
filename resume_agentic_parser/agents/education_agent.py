class EducationAgent:
    def run(self, text):
        keywords = ["B.Sc", "M.Sc", "Bachelor", "Master", "PhD", "Diploma", "University", "College"]
        return "; ".join([line.strip() for line in text.split("\n") if any(k in line for k in keywords)])
