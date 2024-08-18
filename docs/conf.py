# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

# -- Path setup

import os
import sys

sys.path.insert(0, os.path.abspath("../"))


# -- Project information

project = "pixiv-api-bypass-sni"
copyright = "2024, sekatol"
author = "sekatol"
release = "1.0.1"

# -- General configuration

extensions = ["sphinx.ext.autodoc", "sphinx_rtd_theme"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ".rst"
master_doc = "index"

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
