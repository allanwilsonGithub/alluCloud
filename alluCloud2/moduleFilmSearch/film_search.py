#/usr/bin/env python

import json
import urllib2

def search_words_return_titles(search_term):
    url = "http://www.omdbapi.com/?s={}&y=&plot=short&r=json".format(search_term)
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