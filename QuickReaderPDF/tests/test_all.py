import sys
import os
from fpdf import FPDF
from QuickReaderPDF import pdf_reader,text_to_pdf,create_html,pdf_to_html,remove_html,format_file # noqa: E501
sys.path.append('../')
sys.path.append('./')


def test_pdf_reader(tmp_path):
    file_path = os.path.join(tmp_path, 'test_file.pdf')
    data=[1,2,3,4,5,6]
    pdf = FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("helvetica", size=12)
    for i in str(data):
        pdf.write(5,i)
    pdf.output(file_path)
    assert '[1, 2, 3, 4, 5, 6]'== pdf_reader(file_path)


def test_text_to_pdf(tmp_path):
    file_path = os.path.join(tmp_path, 'test_file.html')
    text="hello"
    text_to_pdf(text,file_path)
    Func = open(file_path,"r+")
    assert Func.read().split() == ['<!DOCTYPE', 'html>', '<html>', '<body>', '<center>', '<p', 'style="color:black;font-size:21px;">', '<b>hel</b>lo', '<br>', '</p>', '</body>', '</html>']# noqa: E501


def test_create_html(tmp_path):
    # Define the file path for the new file
    file_path = os.path.join(tmp_path, 'test_file.html')
    # Call the create_file function with the file path and contents
    create_html(file_path)
    # Check that the file was created
    assert os.path.isfile(file_path)

    
def test_pdf_to_html(tmp_path):
            
    file_path_html = os.path.join(tmp_path, 'test_file.html')
    file_path_pdf = os.path.join(tmp_path, 'test_file.pdf')
    with open(file_path_html, 'wb') as f:
        f.write(b'This is a test.')

    pdf_to_html(file_path_html,file_path_pdf)    
    assert os.path.isfile(file_path_pdf)
    pass

def test_remove_html(tmp_path):
    file_path = os.path.join(tmp_path, 'test_file.html')
    # Create a test file
    with open(file_path, 'w') as f:
        f.write('This is a test.')
    # Call the delete_file function with the file path
    remove_html(file_path)

    # Check that the file was deleted
    assert not os.path.isfile(file_path)
    pass

def test_format_file(tmp_path):
    file_path_html = os.path.join(tmp_path, 'testfile.html')
    with open(file_path_html, 'w') as Func:
        format_file(["Hello"],Func)
        assert os.path.isfile(file_path_html)
