from setuptools import setup


setup(
    name='QuickReaderPDF',
    version="0.3.3",
    install_requires=[
    'pypdf==3.7.0',
    'pdfkit==1.0.0',
    'fpdf==1.7.2',
    'wkhtmltopdf==0.2',
    'beautifulsoup4==4.11.1',
    'pdfminer.six==20221105',
    'requests==2.31.0',
    'weasyprint==58.1',
    ],  
    python_requires='>=3.6',
)