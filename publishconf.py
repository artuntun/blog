#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

#SITEURL = 'http://empiricalstateofmind.github.io/blog'
SITEURL = 'https://andrewmellor.co.uk/blog'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

SOCIAL = SOCIAL + (('rss', SITEURL + '/' + FEED_ALL_ATOM),)

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "empiricalstateofmind"
GOOGLE_ANALYTICS = "UA-49010624-4"
ADDTHIS_PROFILE = 'ra-5477a96408ae534a'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False
