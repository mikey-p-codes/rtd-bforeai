# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'BforeAi API Documentation'
author = 'Patti@bfore.ai'
release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for todo extension ----------------------------------------------

todo_include_todos = True