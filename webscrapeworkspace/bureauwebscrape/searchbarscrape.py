# works for python 2
# modules to read data from urls
import urllib
import urllib2
import string
import sys
from bs4 import BeautifulSoup

# make program look like a browser, user_agent
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

# pass in the word into the search bar a.k.a create html form
values = {'s' :  sys.argv[1]}
# urlencode the word
data = urllib.urlencode(values)
# makes the request/form  
request = urllib2.Request("https://www.dict.cc/", data, headers)
# sends the request/form to the website
response = urllib2.urlopen(request)

# read the html code form the website
the_page = response.read()
# turns the data into string
pool = BeautifulSoup(the_page, "html.parser")

# get BeautifulSoup.ResultSet and return all td with class td7nl
results = pool.findAll('td', attrs={'class' : 'td7nl'})
source = ''
translations = []

# loop through the results
for result in results:
	word = ''
	# for each td's text
	for tmp in result.findAll(text=True):
		word = word + " " + unicode(tmp).encode("utf-8")
	# append data
	if source == '':
		source = word
	else:
		translations.append((source, word))

# print out data
for translation in translations:
	print("%s => %s") % (translation[0], translation[1])
