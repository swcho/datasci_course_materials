__author__ = 'sungwoo'

import urllib
import json

response = urllib.urlopen('http://search.twitter.com/search.json?q=microsoft')
response_json = json.load(response)

print response_json