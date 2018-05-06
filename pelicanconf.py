#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Martin Noah'
SITENAME = 'MartinNoah'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/New_York'

PLUGIN_PATHS = ['C:/Users/mnoah/MartinBlog/themes/pelican-plugins', ]
PLUGINS = ['i18n_subsites',]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


THEME = 'C:/Users/mnoah/MartinBlog/themes/pelican-themes/pelican-bootstrap3'

DEFAULT_LANG = 'English'

ABOUT_ME = "Random blogs about Python, Excel, Web Development, and maybe some hockey (Go Pens!)"
AVATAR = 'images/FuEA2MYH_400x400.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/MixMasterMartin'),
          ('Facebook', 'https://www.facebook.com/martin.noah.98'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
