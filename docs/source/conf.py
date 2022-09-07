# Configuration file for the Sphinx documentation builder.

# -- Project information


import os
import sys
sys.path.insert(0, os.path.abspath('.'))
#import sphinx_rtd_theme
import sphinxcontrib.bibtex
import myst_parser
import sphinxcontrib.apa

project = 'BJPsychBulletin'
Copyright = '2022, Justpsychiatry'
author = 'Justpsychiatry'

#release = '0.1'
#version = '0.1.0'

# -- General configuration



intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx_sitemap',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.apa',
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx_design',
    'sphinx_search.extension',
    'hoverxref.extension',
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
# -- Options for HTML output


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'myst',
}


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = "BJPsych Bulletin Archive"
html_baseurl ='https://justpsychiatry.co.uk/projects/bjpsych-bull/'
bibtex_bibfiles = ['bjpsych.bib']
bibtex_reference_style = 'author_year'
sitemap_filename = "bjpsychmap.xml"
sitemap_url_scheme = "{link}"
hoverxref_auto_ref = True
html_show_copyright = True


rst_epilog = """


 .. admonition:: Copyright Notice
 
     Articles published from BJPsych Bulletin are open-access, published under the terms of creative commons  Attribution licence (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted re-use, distribution, and reproduction in any medium, provided the original work is properly cited.
    The Authors own the copyrights to the individual articles. 
       
"""

hoverxref_roles = [
    'numref',
    'term',
    'abbr',
    'ref',
]


rst_prolog = """
.. meta::
  :journal-id-nlm-ta: BJPsych Bull
  :journal-iso-abbrev: BJPsych Bull
  :journal-publisher-id: BJB
  :journal-title(full): BJPsych Bulletin 
  :issn(print): 2056-4694 
  :issn(epub): 2056-4708 
  :publisher: Cambridge University Press 
  :publisher’s Location: Cambridge, UK 
  :description: The British Journal of Psychiatry.
  :keywords: plaintext, markup language
"""

# -- Options for EPUB output
epub_show_urls = 'footnote'
