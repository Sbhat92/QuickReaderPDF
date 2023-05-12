"Boldens the first three letters of each word"
from bs4 import BeautifulSoup
import requests
import sys
import os
from weasyprint import HTML
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal

def url_parser(url):
    """
    Given a URL, sends a GET request and returns the response object.

    Parameters:
    url (str): The URL to send the GET request to.

    Returns:
    requests.Response: The response object returned by the GET request.
    """

    response = requests.get(url)
    return response

def copy_url(response,html_file):
    """
    Writes the content of the response object to the specified HTML file.

    Parameters:
    response (requests.Response): The response object 
    containing the content to be written. 
    html_file (str): The path and filename of the HTML file to be written.
    """ # noqa: E501
    with open(html_file, "w") as f:
        f.write(response.text)


def html_to_pdf(html_file, pdf_file):
    # Convert HTML to PDF
    HTML(html_file).write_pdf(pdf_file)

def read_html_file(html_file):
    """
    Reads the contents of the specified HTML file and returns
    them as a string.

    Args:
    html_file (str): The path and filename of the HTML file to be read.

    Returns:
    str: The contents of the specified HTML file.
    """ # noqa: E501
    # Load the HTML file
    with open(html_file) as f:
        html_doc = f.read()
        return html_doc

def create_bs_obj(html_doc):
    """
    Given an HTML document, creates a BeautifulSoup object and returns it.

    Parameters:
    html_doc (str): The HTML document to be parsed into a BeautifulSoup object.

    Returns:
    bs4.BeautifulSoup: The BeautifulSoup object created from the HTML document.
    """ # noqa: E501
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup

def bolden_html(soup):
    """
    Given a BeautifulSoup object, finds all text in the HTML
      file and bolds the first three letters of every word.

    Parameters:
    soup (bs4.BeautifulSoup): The BeautifulSoup object representing the HTML document.

    Returns:
    bs4.BeautifulSoup: The modified BeautifulSoup object with bolded text.
    """ # noqa: E501
    # Find all text in the HTML file
    
    # Bold the first three letters of every word using the wrap() method
    for text_node in soup.find_all(string=True):
        words = text_node.split()
        for i, word in enumerate(words):
            if len(word) >= 3 and text_node.parent.name != 'script':
                new_tag = soup.new_tag('b')
                new_tag.string = word[:3]
                words[i] = str(new_tag) + word[3:]
        new_text_node = ' '.join(words)
        text_node.replace_with(BeautifulSoup(new_text_node, 'html.parser'))

    return soup

def write_html(soup,html_file):  
    """
    Given a BeautifulSoup object and an HTML file path,
    writes the modified HTML to the specified file.

    Parameters:
    soup (bs4.BeautifulSoup): The modified BeautifulSoup 
    object to be written to the HTML file.
    html_file (str): The path and filename of the HTML file to be written.
    """      
    # Write the modified HTML to a new file
    with open(html_file, 'w') as f:
        f.write(str(soup))

def remove_html(html_file):
    """
    Deletes the specified HTML file.

    Parameters:
    html_file (str): The path and filename of the HTML file to be deleted
    """
    os.remove(html_file)

def main_func(type = "url", input="sample.pdf", file_name="out.pdf"):
    """
    Converts a PDF file or URL to a PDF file with bold text.

    Args:
        type (str, optional): The type of input.
          Either "url" or "pdf". Defaults to "url".
        input (str, optional): The URL or PDF file path.
          Defaults to "sample.pdf".
        file_name (str, optional): The name of the output PDF file.
          Defaults to "out.pdf".

    Returns:
        None
    """
    if type == "url":
        #User inputs a url to us
        #url = "https://americanliterature.com/author/philip-k-dick/short-story/the-eyes-have-it"
        html_file = "htmltoPDF.html"
        response = url_parser(str(input))
        copy_url(response,html_file)
        
        pass
    elif type == "pdf":
        # Define a default font name and font size
        default_font_name = "Arial"
        default_font_size = 12
        html_file = "htmltoPDF.html"
        # Extract the text and formatting information from the PDF
        html = ""
        current_y = None
        for page_layout in extract_pages(input):
            for element in page_layout:
                if isinstance(element, LTTextBoxHorizontal):
                    # Check if the vertical coordinate has changed, indicating a new paragraph # noqa: E501
                    if current_y is None:
                        current_y = element.y0
                        html += "<p>"
                    elif element.y0 != current_y:
                        current_y = element.y0
                        html += "</p><p>"

                    # Get the font size and font name if available
                    font_size = element.size if hasattr(element, 'size') else default_font_size # noqa: E501
                    font_name = element.fontname if hasattr(element, 'fontname') else default_font_name # noqa: E501

                    # Check if the font weight is bold and add the appropriate style to the HTML output # noqa: E501
                    font_style = "font-style:italic;" # noqa: F821
                    # Check for italic and underline attributes and add to the HTML output # noqa: E501
                    if element.get_text().startswith('<i>') and element.get_text().endswith('</i>'):# noqa: E501
                        font_style += "font-style:italic;" # noqa: F821
                    if element.get_text().startswith('<u>') and element.get_text().endswith('</u>'):# noqa: E501
                        font_style += "text-decoration:underline;" # noqa: F821

                    # Add the text and formatting information to the HTML output
                    html += f'<span style="font-size:{font_size}px; font-family:{font_name}; {font_style}">{element.get_text()}</span>' # noqa: E501

            # Add paragraph tags to the end of the page
            html += "</p>"

        # Wrap the HTML output in a basic HTML document structure
        html = f'<!DOCTYPE html><html><head></head><body>{html}</body></html>'

        # Save the final HTML file
        with open(html_file, "w") as output_file:
            output_file.write(html)

    else:
        print("please enter a valid format. PDF or URL")
        exit(0)

    html_doc = read_html_file(html_file)
    soup = create_bs_obj(html_doc)
    soup = bolden_html(soup)
    write_html(soup,html_file)
    html_to_pdf(html_file, file_name)
    remove_html(html_file)

if __name__ == "__main__":
    print("Executed when invoked directly")
    main_func(sys.argv[1], sys.argv[2],sys.argv[3])
