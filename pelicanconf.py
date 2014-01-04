#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nico'
SITENAME = 'Beerfactory'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME="theme"
PLUGINS = ["cat_display_name","sitemap",]

DEFAULT_PAGINATION=5
DISQUS_SITENAME='beerfactory'

#Categories display name mapping
CAT_DISPLAY_NAME_MAP = {'news': 'News',
                        'nicohb': "Nico homebrewing",
                        'yeah': "This is a test"}
#Categories subtitle mapping (subtitles are used in category page)
CAT_SUBTITLE_MAP = {'news': 'General news about the project',
                        'nicohb': "Personal blog from the project owner, about computer and beer.",
                        'yeah': "This is a test"}
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
MENUITEMS= (('Forum', 'http://forum.beerfactory.org/'),)