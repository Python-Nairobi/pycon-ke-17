#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Python Nairobi'
SITENAME = u'PyConKE'
TAGLINE = ''
SITEURL = ''
DESCRIPTION = """
PyConKe will be the first in a series of annual gatherings of software developers,
techies, business people, startups, learning institutions, students and other
organizations and individuals that use or otherwise have an interest/stake in
the Python programming language and its ecosystem
"""

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
#    ('Schedule', '/schedule'),
    ('Recent Developments', '/#developments'),
#    ('Sponsorship', '/sponsorship'),
    ('Call for Proposals', '/call_for_proposals'),
    ('Volunteering', '/call_for_volunteers'),
#    ('About', '/about'),
)

VOLUNTEER_LINK = "call_for_volunteers"
PROPOSALS_LINK = ""
SPONSOR_LINK = "mailto:sponsorthis@pycon.or.ke"
TOPICS = (
    (
        'fa-globe',
        'Web, Music &amp; Animation',
        'Pythonic web frameworks, scripting in animation with Blender '
        'and coding music in Py with sonicpi. Plenty of talks and tutorials '
        'on these to get you started.'
    ),
    (
        'alt fa-bar-chart-o',
        'Data Science &amp; AI',
        'Stats crunching with Pandas &amp; co. and ML with with tools like Tensorflow. '
        'Come partake in some pythonic stats &amp; AI '
        '(just don''t let what you subsequently create become self aware)'
    ),
    (
        'alt2 fa fa-microchip',
        'Internet of Things',
        'Python in my IoT? It''s more likely than you think! Featured at the conference'
        'will be talks and presentations on (micro)python on assorted hardware'
        'with example applications.',
    )
)
SPONSORS = (
    (
        "https://jumo.world",
        "images/jumo.png",
        "Jumo World"
    ),
    (
        "https://usiu.ac.ke",
        "images/usiu.png",
        "Jumo World",
    ),
    (
        "https://ona.io",
        "images/ona.png",
        "ONA",
    )
)
ORGANIZERS = (
    (
        "http://meetup.com/Python-Nairobi",
        "images/pynbo.jpg",
        "Python Nairobi",
    ),
    (
        "http://tunapanda.org",
        "images/tunapanda.jpg",
        "Tunapanda Institute",
    )
)

STATIC_PATHS = [
    'images',
    'js',
    'css',
    'extra/robots.txt',
    'CNAME',
    'README.md',
]
