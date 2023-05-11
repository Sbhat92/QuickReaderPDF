
  

# QuickReaderPDF

  

  

License:

  

![license](https://img.shields.io/badge/license-MIT-blue)

  

  

Issues:

  

![issues](https://img.shields.io/github/issues/Sbhat92/QuickReaderPDF)

  

  

Pypi

  

[![PyPI](https://img.shields.io/pypi/v/QuickReaderPDF)](https://pypi.org/project/QuickReaderPDF/)

  

# overview

  

  

Build:

  

[![Linting, Testing Status](https://github.com/Sbhat92/QuickReaderPDF/actions/workflows/setup.yaml/badge.svg)](https://github.com/Sbhat92/QuickReaderPDF/actions/workflows/setup.yaml)

  

  

COde coverage:

  

[![Codecov](https://codecov.io/gh/Sbhat92/QuickReaderPDF/branch/main/graph/badge.svg)](https://codecov.io/gh/Sbhat92/QuickReaderPDF)

  

  

### Read a PDF up to 20% faster!

  

  

## Description

  

  

This package converts a pdf or a html file that the user wants to read to an new pdf file, which can be read faster! The idea is ["bionic reading"](https://www.huffingtonpost.co.uk/entry/what-is-bionic-reading-does-it-work_uk_628749a3e4b05cfc268a59ff), where we bold the first three letters of every word. We hope you enjoy reading your files faster!

  

  

## Features:

  

  

The user can input a pdf file or a html file, and `QuickReaderPDF` will output a pdf with the first three letters boldened.

  

  

## Installation

  

  

To install, simply open a terminal and type:

  

`pip install QuickReaderPDF`

  

  

You're ready to go!

  

  

## Usage

  

  

## Usage

1. Open a terminal in the location of the pdf file you want. 
2. Use the provided functions to convert a PDF file or URL to a PDF file with bold text:

   To convert a URL to a PDF file with bold text:


   url =   `"https://example.com"`

   `python <path to directory with package/pdfeditor.py> <url> url <name of new pdf>`

   To convert a PDF file to a PDF file with bold text:

      input_file = "input.pdf"
      `python <path to directory with package/pdfeditor.py> <pdf> input_file <name of new pdf>`

   Make sure to replace "https://example.com" with the desired URL and "input.pdf" with the path to your input PDF file.


  

  

## Example

  
1. You can convert any url, for example: [A great short story](https://americanliterature.com/author/philip-k-dick/short-story/the-eyes-have-it) and convert it into a pdf like:

  <img  src="https://drive.google.com/uc?id=1YfQ1A8f25FnTiMjLNwGDHZQs5S3Zsw6D">

2. You can also use QuickReaderPDF to convert a pdf into a boldened pdf.
