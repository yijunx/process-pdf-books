from PyPDF2 import PdfReader


class PyPDF2PDFParser:

    def __init__(self, path: str):
        self.reader = PdfReader(path)

    def get_generic_info(self):
        
        meta = self.reader.metadata

        print("Total Pages: ", len(self.reader.pages))
        # All of the following could be None!
        print("Author: ", meta.author)
        print("Creator: ", meta.creator)
        print("Producer: ", meta.producer)
        print("Subject: ", meta.subject)
        print("Title: ", meta.title)

    def read_page(self, page_number: int):
        page = self.reader.pages[page_number]
        print(page.extract_text())


if __name__ == "__main__":
    book1_path = "pdfs/南北方音_首师大.pdf"
    p = PyPDF2PDFParser(path=book1_path)
    p.get_generic_info()
    p.read_page(100)