#/usr/bin/env python

import json
import urllib2
from urllib2 import URLError

'''
Errors to catch...
1) No results:                        JSON format error, None
2) Bad URL or no network:             urllib2.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
'''

def search_words_return_titles(search_term):
    try:
        url = "http://www.omdbapi.co/?s={}&y=&plot=short&r=json".format(search_term)
    except URLError, e:
        print e.reason
    response = json.load(urllib2.urlopen(url))
    return response

def present_data(response):
    try:
        for x in response['Search']:
            print x['Title']

    except (ValueError, KeyError, TypeError):
        print "JSON format error"

search_term = raw_input("Search for a word in the film title: ") or "Star"
search_result = search_words_return_titles(search_term)
print present_data(search_result)