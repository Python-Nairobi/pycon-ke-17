#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Python Nairobi'
SITENAME = u'PyConKE'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/python-nairobi'),
    ('twitter', 'https://twitter.com/pynbo'),
    ('meetup', 'https://www.meetup.com/Python-Nairobi/'),
    ('file-text', 'http://blog.pynbo.or.ke/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pyconke17-dopetrope"
NAVITEMS = (
    ('PyConKe 17', '/'),
    ('Registration', '/registration'),
    ('Schedule', '/schedule'),
#    ('Sponsorship', '/sponsorship'),
    ('Call for Proposals', '/call_for_proposals'),
    ('Volunteering', '/call_for_volunteers'),
    ('CoC', '/coc'),
    ('Recent Developments', '/#developments'),
#    ('About', '/about'),
)

VOLUNTEER_LINK = "call_for_volunteers"
PROPOSALS_LINK = ""
SPONSOR_LINK = "mailto:sponsorthis@pycon.or.ke"

STATIC_PATHS = [
    'images',
    'js',
    'css',
    'extra/robots.txt',
    'CNAME',
    'README.md',
]
