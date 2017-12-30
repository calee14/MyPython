# import libraries
import urllib
import urllib2
from bs4 import BeautifulSoup
from BLSContent import BLSContent
import json

# scrape occupations
# make program look like a browser, user_agent
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }
# search keys
search_urls = []
# get json file name 
jsonfilename = "occupationlinks.json"
# open json file as var json_data
with open(jsonfilename) as json_data:
	# store it in variable d
	d = json.load(json_data)
	# get second object
	for link in d:
		for child in link:
			title = link[child]
			for url in title:
				blslink = title[url]
				search_urls.append(blslink)

search_url = search_urls[1]
page = urllib.urlopen(search_url)
soup = BeautifulSoup(page, 'html.parser')
contents = soup.find('div', attrs={'id' : 'panes'})
occupation_info = []
for content in contents:
	article = content.find("article")
	try: 
		for items in article:
			continue
	except:
		continue
	for items in article:
		# to keep track if we added a class or not
		addedContainer = False
		try:
			# loop all types of headers
			for i in range(1,7):
				# if node is a h tag
				if items.name == 'h'+str(i):
					# make a new blscontainer object
					title = items.text
					# give it a new title
					new_container = BLSContent(title)
					# add the new container to the temp container
					occupation_info.append(new_container)
					# append the text of the title and break the loop
					addedContainer = True
					break
			# if its content add it
			if addedContainer == False:
				if items.name == 'table':
					print 'we found the table'
				# get last appended container and add to it
				occupation_info[-1].addChild(items.text)
		except:
			pass
print occupation_info[7].children
jsonstuff = []
for info in occupation_info:
	json_data = {
		info.title : info.children
	}
	jsonstuff.append(json_data)
json_data = json.dumps(jsonstuff, indent=4)
filename = "info.json"
f = open(filename, 'w')
f.write(json_data)




