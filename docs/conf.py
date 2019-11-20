"""Read The Docs configuration."""
# -*- coding: utf-8 -*-

project = 'Area4'
project_lc = project.lower()
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
    'sphinx.ext.extlinks'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of doc file names.
source_suffix = '.rst'

# The main page
master_doc = 'index'

# DO NOT CHANGE.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

# Do NOT change:
pygments_style = 'sphinx'

# The theme to use for HTML
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, copyright is shown in the HTML footer
html_show_copyright = True

html_show_sphinx = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'Area4doc'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '12pt',
}

latex_documents = [
    (master_doc, 'Area4.tex', 'Area4 Documentation',
     'RDIL', 'manual'),
]

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'area4', 'Area4 Documentation',
     [author], 1)
]

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
# dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Area4', 'Area4 Documentation',
     author, 'Area4', 'One line description of project.',
     'Miscellaneous'),
]

epub_title = project

# Files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

intersphinx_mapping = {'https://docs.python.org/': None}
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
