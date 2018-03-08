from TableScraper import TableScraper
import json
from collections import namedtuple

# make program look like a browser, user_agent
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

def scrape_main_table():
	# scrape the main occupations table
	page_link = 'https://www.bls.gov/emp/ep_table_101.htm'
	page_title = 'MajorOccupations'
	classIdentifier = 'class'
	idName = 'regular'
	linkFileName = 'occupationlinks.json'
	dataFileName = 'occupations.json'
	# run it 
	retriever = TableScraper(page_link, page_title, classIdentifier, idName, linkFileName, dataFileName)
	retriever.scrape()

def scrape_ooh_table():
	# scrape the bls.gov/ooh tables
	# search keys
	search_urls = []
	# get json file name 
	jsonfilename = "links.json"
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
					SearchUrl = namedtuple('SearchUrl', 'title url')
					searchData = SearchUrl(child, blslink)
					search_urls.append(searchData)
					# print searchData.title + "child"
					# print searchData.url
	for search_url in search_urls:
		page_link = search_url.url #'https://www.bls.gov/emp/ep_table_101.htm'
		page_title = search_url.title
		classIdentifier = 'class'
		idName = 'display'
		linkFileName = 'occupationlinks.json'
		dataFileName = 'occupations.json'
		# run it 
		retriever = TableScraper(page_link, page_title, classIdentifier, idName, linkFileName, dataFileName)
		retriever.scrape()

def scrape_careers():
	# scrape the bls.gov/ooh tables
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
					SearchUrl = namedtuple('SearchUrl', 'title url')
					searchData = SearchUrl(child, blslink)
					search_urls.append(searchData)
	for search_url in search_urls:
		page_link = search_url.url #'https://www.bls.gov/emp/ep_table_101.htm'
		page_title = search_url.title
		classIdentifier = 'id'
		idName = 'quickfacts'
		linkFileName = None #'occupationlinks.json'
		dataFileName = None #'occupations.json'
		# run it 
		retriever = TableScraper(page_link, page_title, classIdentifier, idName, linkFileName, dataFileName)
		retriever.scrape()

if __name__ == '__main__':
	scrape_main_table()
	scrape_ooh_table() 
	scrape_careers()
