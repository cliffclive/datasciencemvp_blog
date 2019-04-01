#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cliff Clive'
SITENAME = 'Data Science MVP'
SITEURL = ''

OUTPUT_PATH = '../output'
PLUGIN_PATHS = ['plugins', ]
PLUGINS = ['i18n_subsites', ]
THEME = 'theme'
BOOTSTRAP_THEME = 'yeti'
PYGMENTS_STYLE = 'friendly'

LINKS = (('Metis', 'https://www.thisismetis.com/'),
        ('MixCloud', 'https://www.mixcloud.com/dj-conxn/'),)
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/cliffordclive/'),
        ('Twitter', 'https://twitter.com/cliffclarkclive'),)

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['img', 'pdf']

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
