# import libraries
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import json
from BLSHeader import HeaderOccupation

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

# make program look like a browser, user_agent
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

# set url
url = "https://www.bls.gov/emp/ep_table_101.htm"
# open the url
page = urllib.urlopen(url)
# run BeautifulSoup on the html
soup = BeautifulSoup(page, 'html.parser')
# find table
table = soup.find('table', attrs={'class' : 'regular'})
# find header
header = table.find('thead').find('tr')
# scrape the header of table
# list
header_list = []
# loop through each row
count = 0
# get the headers
for head in header:
	try:
		title = head.find('strong').text.encode('utf-8')
		colspan = int(head['colspan'])
		header = ''
		array = []
		for header in header_list:
			array.append(header.requests_objects)
		header = HeaderOccupation(colspan, title, count, array)
		count += 1
		header_list.append(header)
	except Exception as e:
		# print e
		pass
# scrape the contents of the header
contents = table.find('tbody')
for row in contents:
	children = []
	# for item in row:
	try:
		children = row.find_all('p')
		# children = list(set(children))
		# children = f7(children)
		print children
	except Exception as e:
		# print e
		pass
	else:
		# if try is succuessful
		for header in header_list:
			for num in header.requests_objects:
				header.children.append(str(children[num].text))

filename = "test.txt"
f = open(filename, "w")
for header in header_list:
	for child in header.children:
		f.write(''+header.title+' '+child+'\n')
