#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Lix'

import urllib
import urllib2
import re

page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
headers = { 'User-Agent' : user_agent }

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    # pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)
    # pattern = re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2.*?content">(.*?)</div></a>', re.S)
    pattern = re.compile(r'<div.*?clearfix">.*?<h2>(.*?)</h2.*?content">.*?an>(.*?)</.*?number">(.*?)</', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item[0], item[1], item[2]
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print 'reason ---->' + e.reason