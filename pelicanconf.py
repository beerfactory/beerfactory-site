#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nico'
SITENAME = 'Beerfactory'
SITEURL = 'http://www.beerfactory.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Forum brassageamateur.com', 'http://www.brassageamateur.com/forum/'),
          )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME="theme"
PLUGINS = ["sitemap","thumbnail"]

DEFAULT_PAGINATION=5
DISQUS_SITENAME='beerfactory'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

GOOGLE_ANALYTICS="UA-37658015-2"

MENUITEMS = [('Blog', '/blog/index.html')]

USE_FOLDER_AS_CATEGORY=False
AUTHORS_SAVE_AS=False
TAGS_SAVE_AS=False
DOCUTILS_SETTINGS = {'math_output': 'mathjax'}
STATIC_PATHS = [
    'robots.txt', 'images'
    ]

DATE_FORMATS = {
    'fr': '%d %B %Y',
}

DEFAULT_DATE_FORMAT = DATE_FORMATS['fr']

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'
TAGS_SAVE_AS = ''
INDEX_SAVE_AS='blog/index.html'
ARCHIVES_SAVE_AS='blog/archives.html'
CATEGORIES_SAVE_AS = ''  
ARTICLE_URL = '/blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = '/blog/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}.html'
DRAFT_URL = '/blog/drafts/{slug}.html'
DRAFT_SAVE_AS = 'blog/drafts/{slug}.html'
DRAFT_LANG_URL = '/blog/drafts/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'blog/drafts/{slug}-{lang}.html'
PAGE_URL = '/{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
CATEGORY_URL = '/blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
TAG_URL = '/blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
AUTHOR_URL = '/blog/author/{slug}.html'
AUTHOR_SAVE_AS = 'blog/author/{slug}.html'