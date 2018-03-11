from TextScraper import TextScraper
import json
from collections import namedtuple

# make program look like a browser, user_agent
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

def scrapeSummaries():
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
		classIdentifier = 'class'
		idName = 'display'
		scrapetext = TextScraper(page_link, None, None)
		scrapetext.setHeadersText('h4', 'p')
		scrapetext.scrapeArea('center-content')
		scrapetext.addToDatabase(page_title.strip() + '_summary')
		# linkFileName = 'occupationlinks.json'
		# dataFileName = 'occupations.json'
if __name__ == '__main__':
	scrapeSummaries()