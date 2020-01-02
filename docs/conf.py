"""Sphinx configuration."""
# -*- coding: utf-8 -*-

project = 'Area4'
copyright = '2018-present, Reece Dunham.'
author = 'Reece Dunham'

# Do NOT change:
version = ''
release = ''

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of doc file names.
source_suffix = '.rst'

# The main page
master_doc = 'index'

language = 'en'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_show_copyright = True

html_show_sphinx = False

htmlhelp_basename = 'Area4doc'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '12pt'
}

latex_documents = [
    (
        master_doc,
        'Area4.tex',
        'Area4 Documentation',
        author,
        'manual'
    )
]

man_pages = [
    (
        master_doc,
        'area4',
        'Area4 Documentation',
        [author],
        1
    )
]

texinfo_documents = [
    (
        master_doc,
        project,
        'Area4 Documentation',
        author,
        project,
        'Dividers in Python, the easy way!',
        'Miscellaneous'
    )
]

epub_title = project

epub_exclude_files = ['search.html']

intersphinx_mapping = {
    'https://docs.python.org/3/': None
}

html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
