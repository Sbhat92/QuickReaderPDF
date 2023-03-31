import os
from unittest.mock import patch
import unittest 
from unittest import mock
from unittest.mock import MagicMock
from fpdf import FPDF
from unittest.mock import patch, mock_open, Mock
import sys
sys.path.append('../')
from pdfeditor import *

#unit test pdf_reader

# def test_pdf_reader():
#     read_data = "data"
#     mock_open = mock.mock_open(read_data=read_data)
#     with mock.patch('builtins.open', mock_open) as mock_file:
#         assert open("path/to/open").read() == "data"
#     mock_file.assert_called_with("path/to/open")

def test_pdf_reader(tmp_path):
    read_data = "data"
    file_path = os.path.join(tmp_path, 'test_file.pdf')
    data=[1,2,3,4,5,6]
    pdf = FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for i in str(data):
        pdf.write(5,i)
    pdf.output(file_path)
    assert '[1, 2, 3, 4, 5, 6]'==pdf_reader(file_path)



# def test_read_pdf(tmp_path):
#     # Create a temporary PDF file with some contents
#     file_path = os.path.join(tmp_path, 'test_file.pdf')
#     with open(file_path, 'wb') as f:
#         f.write(b'This is a test.')

#     # Call the read_pdf function with the temporary file path
#     pdf_contents = read_pdf(file_path)

#     # Check that the contents of the PDF were read correctly
#     assert pdf_contents == b'This is a test.'

def test_create_html(tmp_path):
    # Define the file path for the new file
    file_path = os.path.join(tmp_path, 'test_file.html')
    # Call the create_file function with the file path and contents
    create_html(file_path)
    # Check that the file was created
    assert os.path.isfile(file_path)



def test_text_to_html():
    pass
    
    
def test_pdf_to_html(tmp_path):
            
    file_path_html = os.path.join(tmp_path, 'test_file.html')
    file_path_pdf = os.path.join(tmp_path, 'test_file.pdf')
    with open(file_path_html, 'wb') as f:
        f.write(b'This is a test.')

    pdf_to_html(file_path_html,file_path_pdf)    
    assert os.path.isfile(file_path_pdf)
    pass

def test_remove_html():
    file_path = os.path.join("", 'test_file.html')
    # Create a test file
    with open(file_path, 'w') as f:
        f.write('This is a test.')
    # Call the delete_file function with the file path
    remove_html('test_file.html')

    # Check that the file was deleted
    assert not os.path.isfile(file_path)
    pass

def test_format(tmp_path):
    file_path_html = os.path.join(tmp_path, 'testfile.html')
    with open(file_path_html, 'w') as Func:
        format(["Hello"],Func)
        assert os.path.isfile(file_path_html)
        



