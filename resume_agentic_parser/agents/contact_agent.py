import re

class ContactAgent:
    def run(self, text):
        email = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
        phone = re.findall(r'\+?\d[\d\s\-\(\)]{8,}\d', text)
        return {
            "Email": email[0] if email else "Not found",
            "Phone": phone[0] if phone else "Not found"
        }
