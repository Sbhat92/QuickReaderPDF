import sys
import os
from weasyprint import HTML
import pypdf
from QuickReaderPDF import url_parser,copy_url,html_to_pdf,read_html_file,create_bs_obj,bolden_html,write_html,main_func # noqa: E501
sys.path.append('../')
sys.path.append('./')


def test_url_parser():   
    assert str(url_parser("https://google.com")) == '<Response [200]>'

def test_copy_url(tmp_path):
    file_path = os.path.join(tmp_path, 'test_file.html')
    copy_url(url_parser("https://httpbin.org/get"),file_path)
    with open(file_path, "r") as f:
        html_data = f.read()
    assert type(html_data) == str

def test_html_to_pdf(tmp_path):
    # Define the file path for the new file
    html_file_path = os.path.join(tmp_path, 'test_file.html')
    pdf_file_path = os.path.join(tmp_path, 'test_file.pdf')
    # Call the create_file function with the file path and contents
    f = open(html_file_path,'w')
    message = """<html>
    <head></head>
    <body><p>Hello World!</p></body>
    </html>""" # noqa: E501
    f.write(message)
    f.close()
    html_to_pdf(html_file_path,pdf_file_path)
    # Check that the file was created
    assert os.path.isfile(pdf_file_path)

    
def test_read_html_file(tmp_path):            
    file_path_html = os.path.join(tmp_path, 'test_file.html')
    f = open(file_path_html,'w')
    message = """<html>
    <head></head>
    <body><p>Hello World!</p></body>
    </html>""" # noqa: E501
    f.write(message)
    f.close()
    val = read_html_file(file_path_html)    
    assert val == message

def test_bolden_html(tmp_path):
    file_path_html = os.path.join(tmp_path, 'test_file.html')
    f = open(file_path_html,'w')
    message = """<html>
    <head></head>
    <body><p>Hello World!</p></body>
    </html>""" # noqa: E501
    f.write(message)
    f.close()
    with open(file_path_html) as f:
        html_doc = f.read()
    soup = create_bs_obj(html_doc)
    soup = bolden_html(soup)
    assert str(soup) == "<html><head></head><body><p><b>Hel</b>lo <b>Wor</b>ld!</p></body></html>" # noqa: E501


def test_write_html(tmp_path):
    file_path_html = os.path.join(tmp_path, 'testfile.html')
    write_html("<html><head></head><body><p><b>Hel</b>lo <b>Wor</b>ld!</p></body></html>",file_path_html)# noqa: E501
    val = read_html_file(file_path_html)    
    assert val == "<html><head></head><body><p><b>Hel</b>lo <b>Wor</b>ld!</p></body></html>"# noqa: E501

def test_main_func(tmp_path):
    file_path_html = os.path.join(tmp_path, 'test_file.html')
    file_path_pdf = os.path.join(tmp_path, 'test_file.pdf')
    f = open(file_path_html,'w')
    message = """<html>
    <head></head>
    <body><p>Hello World!</p></body>
    </html>""" # noqa: E501
    f.write(message)
    f.close()
    HTML(file_path_html).write_pdf(file_path_pdf)
    main_func("pdf",file_path_pdf, "out.pdf")
    l = [] # noqa: E741
    with open('out.pdf', 'rb') as f:
        # Create a PdfFileReader object to read the PDF
        pdf_reader = pypdf.PdfReader(f)
        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)
        # Loop over each page in the PDF
        for page_num in range(num_pages):
            # Get the page object
            page = pdf_reader.pages[page_num]
            # Extract the text from the page
            page_text = page.extract_text()
            # Print the page number and text
            l.append(page_text)
    os.remove("out.pdf")
    assert str(l[0]) == """html\nHello World!"""