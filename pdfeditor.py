from pypdf import PdfReader
import pdfkit
import os
import sys


def pdf_reader(file):

    doc = ""
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    for n in range(number_of_pages):
        page = reader.pages[n]
        text = page.extract_text()
        doc += text
    return doc


def create_html(filename):
    Func = open(filename, "x")
    Func.close()


def format(splitted, Func):
    for line in splitted:
        words = line.split(" ")
        for i in words:
            if len(i) > 3:
                highlight = i[0:3]
                nonhighlight = i[3:]
                Func.write("<b>")
                Func.write(highlight)
                Func.write("</b>")
                Func.write(nonhighlight)
                Func.write(" ")

        Func.write("<br>")


def text_to_pdf(text, html_file):
    splitted = text.split('\n')
    create_html(html_file)
    Func = open(html_file, "r+")

    Func.write("""<!DOCTYPE html>
                <html>
                <body>
                <center>
                <p style="color:black;font-size:21px;">
                """)
    format(splitted, Func)
    Func.write("""
    </p>
    </body>
    </html>""")
    Func.close()


def pdf_bolden(file, html_file):
    doc = pdf_reader(file)
    text_to_pdf(doc, html_file)


def pdf_to_html(html_file, file_name):
    pdfkit.from_file(html_file, file_name)


def remove_html(html_file):
    os.remove(html_file)


def main(file="sample.pdf", file_name="out.pdf"):
    html_file = "htmltoPDF.html"
    pdf_bolden(file, html_file)
    pdf_to_html(html_file, file_name)
    remove_html(html_file)


if __name__ == "__main__":
    print("Executed when invoked directly")
    main(sys.argv[1], sys.argv[2])

# run pytest --cov -report
