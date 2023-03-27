from pypdf import PdfReader
from fpdf import FPDF
import pdfkit
import os

file = "sample.pdf"
file_name = "out.pdf"

def pdf_reader(file):
    doc=""
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    for n in range(number_of_pages):
        page = reader.pages[n]
        text = page.extract_text()
        doc += text    
    return doc


def text_to_pdf(text, filename):
        splitted = text.split('\n')
        Func = open("html_from_pdf.html", "x")
        Func.close()

        Func = open("html_from_pdf.html","r+")

        Func.write("""<!DOCTYPE html>
                    <html>
                    <body>
                    <center>
                    <p style="color:black;font-size:21px;">
                    
                    """)
        
        for line in splitted:           
            words=line.split(" ")
            for i in words:
                 if len(i)>3:
                      highlight=i[0:3]
                      nonhighlight=i[3:]
                      Func.write("<b>")
                      Func.write(highlight)
                      Func.write("</b>")
                      Func.write(nonhighlight)
                      Func.write(" ")

            Func.write("<br>")
            Func.write("<br>")
                    
        Func.write("""
        </p>
        </body>
        </html>""")
        Func.close()


def pdf_bolden(file):
    doc=pdf_reader(file) 
    text_to_pdf(doc,"output.pdf")

def pdf_to_html(file_name):
     pdfkit.from_file('html_from_pdf.html', file_name)

pdf_bolden(file)

pdf_to_html(file_name)

os.remove("html_from_pdf.html")