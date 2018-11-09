#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Martin Noah'
SITENAME = 'Martin Noah'
SITEURL = 'https://martinnoah.com'

PATH = 'content'

#CUSTOM_CSS = 'static/css/custom.css'

STATIC_PATHS = ['images', 'extra']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}

TWITTER_CARDS = True
USE_OPEN_GRAPH = True
OPEN_GRAPH_IMAGE = 'images/FuEA2MYH_400x400.jpg'

TIMEZONE = 'America/New_York'

PLUGIN_PATHS = ['C:/Users/mnoah/MartinBlog/themes/pelican-plugins', ]
PLUGINS = ['i18n_subsites',
			'share_post',
            'tag_cloud'
		]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


#DISQUS_SITENAME = "<https://martinnoah.disqus.com>"
DISQUS_SITENAME = "martinnoah"

THEME = 'C:/Users/mnoah/MartinBlog/themes/~/pelican-themes/pelican-bootstrap3'

DEFAULT_LANG = 'English'

ABOUT_ME = "Random tutorials and blog posts about Python, Excel, Web Development, and maybe some hockey (Go Pens!)"
#AVATAR = 'images/FuEA2MYH_400x400.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
 #        ('Python.org', 'http://python.org/'),
  #       ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/MixMasterMartin'),
          ('Facebook', 'https://www.facebook.com/martin.noah.98'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

GOOGLE_ANALYTICS = 'UA-118771828-1'

#SITELOGO = 'images/favicon.png'
#SITELOGO_SIZE = 32
#FAVICON = 'images/favicon.png'
DISPLAY_TAGS_ON_SIDEBAR = True
#DISPLAY_CATEGORIES_ON_SIDEBAR = True

ADDTHIS_PROFILE = 'ra-5b01709f0c3abefa'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
        },
        'markdown.extensions.extra': {},
        # optionally, more extensions,
        # e.g. markdown.extensions.meta
    },
    'output_format': 'html5',
}


#GOOGLEFONT = 'https://fonts.googleapis.com/css?family=IM+Fell+French+Canon+SC|Lato'