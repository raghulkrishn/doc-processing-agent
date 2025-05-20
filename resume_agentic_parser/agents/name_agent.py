import spacy
nlp = spacy.load("en_core_web_sm")

class NameAgent:
    def run(self, text):
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ == "PERSON" and text.index(ent.text) < 200:
                return ent.text
        return "Not found"
