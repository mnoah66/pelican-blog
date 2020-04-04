#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
try:
    from pelican.contents import Draft
except ImportError:
    from pelican.contents import Article as Draft

AUTHOR = 'Martin Noah'
SITENAME = 'Martin Noah'
SITEURL = 'https://martinnoah.com'

PATH = 'content'

CUSTOM_CSS = 'static/custom.css'

STATIC_PATHS = ['images', 'extra/custom.css']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

TWITTER_CARDS = True
USE_OPEN_GRAPH = True
OPEN_GRAPH_IMAGE = 'images/FuEA2MYH_400x400.jpg'

TIMEZONE = 'America/New_York'

PLUGIN_PATHS = ['themes/pelican-plugins', ]
PLUGINS = ['i18n_subsites',
			'share_post',
            'tag_cloud',
            'pelican_javascript'
		]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


DISQUS_SITENAME = "martinnoah"


### Style and theme
THEME = 'themes/~/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly' #Favorite is cosmo so far
BOOTSTRAP_NAVBAR_INVERSE = False
BOOTSTRAP_FLUID = False
BANNER='images/numbers2.jpg'
#BANNER_ALL_PAGES = False
PYGMENTS_STYLE = 'friendly'

DEFAULT_LANG = 'English'

#ABOUT_ME = "Random tutorials and blog posts about Python, Excel, Web Development, and maybe some hockey (Go Pens!)"
#AVATAR = 'images/FuEA2MYH_400x400.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



CC_LICENSE = "CC-BY-NC-SA"

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
 #        ('Python.org', 'http://python.org/'),
  #       ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/MixMasterMartin'),
		   ('LinkedIn', 'https://linkedin.com/in/martin-noah'),
          ('GitHub', 'https://www.github.com/mnoah66'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

GOOGLE_ANALYTICS = 'UA-118771828-1'

#SITELOGO = 'images/favicon.png'
#SITELOGO_SIZE = 32
#FAVICON = 'images/favicon.png'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False
TAG_CLOUD_MAX_ITEMS = 8
TAGS_URL = 'tags.html'
DISPLAY_TAGS_INLINE = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
ARCHIVES_SAVE_AS = 'archives.html'

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