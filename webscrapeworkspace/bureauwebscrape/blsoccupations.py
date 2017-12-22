# import libraries
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import json
from BLSLink import BLSLink
from urlparse import urlparse

# make program look like a browser, user_agent
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

# set url
url = "https://www.bls.gov/ooh"
# open the url
page = urllib.urlopen(url)
# run BeautifulSoup on the html
soup = BeautifulSoup(page, 'html.parser')
# find the occupation list
occupation_table = soup.find('div', attrs={'id' : 'ooh-occupation-list'})
# find all the li
occupations_list = occupation_table.find_all('li')
# list of occupaitons links
occupation_links = []
# loop through the all the li in the occupations list
for occupation in occupations_list:
	# get the a tag
	atag = occupation.find('a')
	# get the link from the a atag
	link = atag['href']
	# parse the domain of the url
	parsed_uri = urlparse(url)
	# get the domain form the string link
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	link = domain+link
	# get the title
	title = atag.text
	# make array of properties
	append_properties = [link, title]
	# create the blslink object
	blslink = BLSLink()
	# add children
	blslink.addChild(append_properties)
	# append object to the array
	occupation_links.append(blslink)

print occupation_links[0].children
filename = "links.json"
f = open(filename, "w")
json_array = []
for link in occupation_links:
	json_array.append(link.createjson())
json_data = json.dumps(json_array, indent=4)
f.write(json_data)
