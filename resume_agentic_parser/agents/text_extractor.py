import fitz  # PyMuPDF

class TextExtractorAgent:
    def run(self, file_path):
        doc = fitz.open(file_path)
        return "\n".join([page.get_text() for page in doc])
