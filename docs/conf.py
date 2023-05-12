# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme
from recommonmark.transform import AutoStructify

project = 'QuickReaderPDF'
copyright = '2023, Shreyas Bhat'
author = 'Shreyas Bhat'
release = '0.1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = "index"
extensions = ['recommonmark', 'sphinx.ext.autodoc']
source_suffix = ['.rst', '.md']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)