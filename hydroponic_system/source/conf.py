# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django


sys.path.insert(0, os.path.abspath('..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'hydroponic_system.settings'

django.setup()

extensions = ["sphinx.ext.autodoc"]

project = 'hydroponic system api'
copyright = '2025, Oleksandr Danylenko'
author = 'Oleksandr Danylenko'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
