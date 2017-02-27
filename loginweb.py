import requests
import urllib2
def login():
	s = requests.session()
	url="http://localhost:8800/"
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	r= response.read()
	print r
login()