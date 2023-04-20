"""Module bolds first three letters of each word."""
from pypdf import PdfReader
import pdfkit
import os
import sys


def pdf_reader(file):
    """
    Read the text content of a PDF file.

    Args:
        file (str): The path to the input PDF file.

    Returns:
        str: The concatenated text content of all pages in the PDF file.
    """
    doc = ""
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    for n in range(number_of_pages):
        page = reader.pages[n]
        text = page.extract_text()
        doc += text
    return doc


def create_html(filename):
    """
    Create a new HTML file with the given filename.

    Args:
        filename (str): The name of the new HTML file to create.
    """
    Func = open(filename, "x")
    Func.close()


def format_file(splitted, Func):
    """
    Apply the text formatting rules to the given text and write the formatted text to an output file.

    Args:
        splitted (List[str]): The text content, split into lines.
        Func (file): The output file to write the formatted text to.
    """
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
    """
    Convert the given text to HTML with the text formatting rules applied, and save it to a file.

    Args:
        text (str): The input text to format and convert to HTML.
        html_file (str): The name of the HTML file to save the formatted text to.
    """
    splitted = text.split('\n')
    create_html(html_file)
    Func = open(html_file, "r+")

    Func.write("""<!DOCTYPE html>
                <html>
                <body>
                <center>
                <p style="color:black;font-size:21px;">
                """)
    format_file(splitted, Func)
    Func.write("""
    </p>
    </body>
    </html>""")
    Func.close()


def pdf_bolden(file, html_file):
    """
    Read the text content of a PDF file, apply the text formatting rules, convert to HTML, and save to a file.

    Args:
        file (str): The path to the input PDF file.
        html_file (str): The name of the HTML file to save the formatted text to.
    """
    doc = pdf_reader(file)
    text_to_pdf(doc, html_file)


def pdf_to_html(html_file, file_name):
    """
    Convert an HTML file to PDF, and save the PDF to a file.

    Args:
        html_file (str): The name of the HTML file to convert to PDF.
        file_name (str): The name of the PDF file to save the converted file to.
    """
    config = pdfkit.configuration()
    print(config)
    try:
        pdfkit.from_file([html_file], file_name, configuration=config)
    except OSError:
        # not present in PATH
        print(OSError)


def remove_html(html_file):
    """
    Remove the specified HTML file.

    Args:
        html_file (str): The name of the HTML file to remove.
    """
    os.remove(html_file)


def main(file="sample.pdf", file_name="out.pdf"):
    """
    Converts a PDF file to a new PDF file where the first three letters of each word are bolded.

    Args:
        file (str): The path to the input PDF file. Defaults to "sample.pdf".
        file_name (str): The name of the output PDF file. Defaults to "out.pdf".
    """
    html_file = "htmltoPDF.html"
    pdf_bolden(file, html_file)
    pdf_to_html(html_file, file_name)
    remove_html(html_file)


if __name__ == "__main__":
    print("Executed when invoked directly")
    main(sys.argv[1], sys.argv[2])

# run pytest --cov -report
