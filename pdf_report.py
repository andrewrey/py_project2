import webbrowser
import os
from fpdf import FPDF
from filestack import Client
from config import api_key


class PdfReport:
    """
    Class that generates a pdf file report with the names of flatmates and their amounts to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill_obj):
        # Create PDF and add page for content with font styling
        pdf = FPDF(orientation='P', unit="pt", format='A4')
        pdf.add_page()
        pdf.set_font(family="Times", size=24, style='B')
        # Place image
        pdf.image(name="files/house.png", w=30, h=30)
        # Create Header Cells for text on PDF document.
        pdf.cell(w=0, h=80, txt=f""""Roommate Billing: {bill_obj.period}""", border=0, ln=1, align="C")
        pdf.line(0, 115, 1000, 115)
        pdf.cell(w=115, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill_obj.period, border=0, ln=1)
        # Update font-size
        pdf.set_font(family="Times", size=14, style="B")
        # Create flatmate1 cells
        pdf.cell(w=115, h=60, txt=flatmate1.name)
        pdf.cell(w=0, h=60, txt=f"""${round(flatmate1.pays(bill_obj, flatmate2), 2)}""", border=1, align="L", ln=1)
        # Empty cell for spacing
        pdf.cell(w=0, h=25, border=0, ln=1)
        # Create flatmate2 cells
        pdf.cell(w=115, h=60, txt=flatmate2.name)
        pdf.cell(w=0, h=60, txt=f"""${round(flatmate2.pays(bill_obj, flatmate1), 2)}""", border=1, align="L", ln=1)
        # Change Directory
        os.chdir("files")
        # Produce PDF Document
        pdf.output(self.filename)
        # open Web Browser
        webbrowser.open(self.filename)


class FileSharer:
    def __init__(self, filepath, key=api_key):
        self.filepath = filepath
        self.api_key = key

    def upload(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

