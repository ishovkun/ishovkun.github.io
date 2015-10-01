#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ishovkun'
SITENAME = u'Igor Shovkun'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "blueidea"
# THEME = "simple"

STATIC_PATHS = [
    'images', 
    # 'extra/robots.txt', 
    'extra/favicon.ico',
]

EXTRA_PATH_METADATA = {
    # 'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Blogroll
LINKS = (('My GitHub', 'https://github.com/ishovkun'),
         ('Energy Geomechanics Laboratory', 'https://faculty.engr.utexas.edu/espinoza'),
         )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
