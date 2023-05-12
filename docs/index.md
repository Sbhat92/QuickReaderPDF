
Welcome to QuickReaderPDF's documentation!
==========================================

  

  

# QuickReaderPDF

  
License:    ![license](https://img.shields.io/badge/license-MIT-blue)				Issues: 		![issues](https://img.shields.io/github/issues/Sbhat92/QuickReaderPDF)	PyPi :     [ ![PyPI](https://img.shields.io/pypi/v/QuickReaderPDF)](https://pypi.org/project/QuickReaderPDF/)	docs status: [![Docs](https://img.shields.io/readthedocs/quickreaderpdf)](https://quickreaderpdf.readthedocs.io/en/latest/index.html)

  
Build: [![Linting, Testing Status](https://github.com/Sbhat92/QuickReaderPDF/actions/workflows/setup.yaml/badge.svg)](https://github.com/Sbhat92/QuickReaderPDF/actions/workflows/setup.yaml)	Code coverage: [![Codecov](https://codecov.io/gh/Sbhat92/QuickReaderPDF/branch/main/graph/badge.svg)](https://codecov.io/gh/Sbhat92/QuickReaderPDF)

  

  

  

## Read a PDF up to 20% faster!

  A library that converts web pages or existing PDFs to new, easier to read PDFs

  

## Description
 

This package converts a pdf or a web page that the user wants to read to an new pdf file, which can be read faster! The idea is ["bionic reading"](https://www.huffingtonpost.co.uk/entry/what-is-bionic-reading-does-it-work_uk_628749a3e4b05cfc268a59ff), where we bold the first three letters of every word. We hope you enjoy reading your files faster!

  

  

## Use case

  

People with ADHD and people who have trouble reading find it easier to concentrate reading files of this type. If you find yourself zoning out while reading often, try this library

  

## Features:

The user can input a pdf file or a html file, and `QuickReaderPDF` will output a pdf with the first three letters boldened.


## Installation


To install, simply open a terminal and type:


`pip install QuickReaderPDF`


  

You're ready to go!

  

  
  

## Usage

  

1. Open a terminal in the location of the pdf file you want.

  

2. Use the provided functions to convert a PDF file or URL to a PDF file with bold text:

  
	### Two use cases:
	
	1. #### URL to PDF boldened

  

		To convert a URL to a PDF file with bold text, say this url:

  

		url = `"https://example.com"`

  

		`python -m pdfeditor.py <url> url <name of new pdf>`

  

		Note that `<url>` is a keyword, which indicates to us that the input is a url.

  

		It will make a new pdf in the same directory, with name `<name of new pdf>`

  

	2. #### PDF to PDF boldened

  

		To convert a PDF file to a PDF file with bold text:

  

		input_file = "input.pdf"

  

		`python -m pdfeditor.py <pdf> input_file <name of new pdf>`

  

		Make sure to replace "https://example.com" with the desired URL and "input.pdf" with the path to your input PDF file.

  
  
  

## Example

  

1. You can convert any url, for example: [A great short story](https://americanliterature.com/author/philip-k-dick/short-story/the-eyes-have-it) and convert it into a pdf:

  

The initial URL looks like:

<img  src="https://drive.google.com/uc?id=1tRH3PCZFTXmvremGEdDzHud1lBLHrWCJ">

  

After we process it, it looks like:

<img  src="https://drive.google.com/uc?id=1YfQ1A8f25FnTiMjLNwGDHZQs5S3Zsw6D">

  

2. You can also use QuickReaderPDF to convert a pdf into a boldened pdf.

```eval_rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```