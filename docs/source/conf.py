# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = u'armpicom'
copyright = u'2021, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.5.3'
release = u'https://github.com/vroncevic/armpicom/releases'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'armpicomdoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'armpicom.tex', u'armpicom Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(master_doc, 'armpicom', u'armpicom Documentation', [author], 1)]
texinfo_documents = [(
    master_doc, 'armpicom', u'armpicom Documentation', author, 'armpicom',
    'One line description of project.', 'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
