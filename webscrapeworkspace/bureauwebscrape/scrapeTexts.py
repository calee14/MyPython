from TextScraper import TextScraper
import json
from collections import namedtuple
from bs4 import Tag, NavigableString, BeautifulSoup
import urllib
import urllib2

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
def scrapeGuidesLinks():
	site= "https://www.learnhowtobecome.org"
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}

	req = urllib2.Request(site, headers=hdr)

	try:
	    page = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
	    print e.fp.read()

	soup = BeautifulSoup(page, 'html.parser')
	careers = soup.find('li', attrs={'class' : 'li-career careerHub'})
	print careers
if __name__ == '__main__':
	# scrapeSummaries()
	scrapeGuidesLinks()