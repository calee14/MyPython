from TextScraper import TextScraper
import json
from collections import namedtuple
from bs4 import Tag, NavigableString, BeautifulSoup
import urllib
import urllib2

def scrapeOccupationSummaries():
	# scrape the summaries
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
	# get the urls of all the careers from bls.gov
	for search_url in search_urls:
		# set the values for the text scraper
		page_link = search_url.url #'https://www.bls.gov/emp/ep_table_101.htm'
		page_title = search_url.title
		classIdentifier = 'class'
		idName = 'display'
		# initialize the text scraper
		# NOTES: need to figure our how to effitiently scrape text
		scrapetext = TextScraper(page_link, None, None)
		# run the functions to scrape the text
		# set headers
		scrapetext.setHeadersText('h4', 'p')
		# scrape the text in the specified area and the specified headers (#hardcode)
		scrapetext.scrapeArea('center-content')
		# create the database with the headers
		headers = ["Job Title", "What Aerospace Engineering and Operations Technicians Do", "Work Environment", "How to Become an Aerospace Engineering and Operations Technician ", "Pay", "Job Outlook", "State and Area Data", "Similar Occupations"]
		# add the data to the database
		scrapetext.addToDatabase(page_title.strip(), headers, "Summaries")
		# scrapetext.dropTableInDatabase(page_title.strip() + '_summary')
		# linkFileName = 'occupationlinks.json'
		# dataFileName = 'occupations.json'
def scrapeGuidesLinks():
	# scrape the guidle links for the careers listed in the learntobecome website
	site= "https://www.learnhowtobecome.org"
	# headers we need to switch around so the website doesn't think we're a bot... but we actually are
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	# make the request to get the html from the website
	# passed in the headers so the server doesn't think we're a bot
	req = urllib2.Request(site, headers=hdr)
	# open the page
	try:
	    page = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
	    print e.fp.read()
	# beautiful soup the page (initialize the html into a beautiful soup class)
	soup = BeautifulSoup(page, 'html.parser')
	# find the links
	careers = soup.find('li', attrs={'class' : 'li-career careerHub'})
	submenu = careers.find('ul', attrs={'class' : 'sub-menu'})
	search_urls = []
	# find all the links in the submenu
	for i in submenu:
		try:
			# find all of the li elements which contain the links
			li_list = i.find_all('li')
			for li in li_list:
				# add the urls to the list of urls
				SearchUrl = namedtuple('SearchUrl', 'title url')
				search_url = SearchUrl(li.find('a').text, li.find('a')['href'])
				search_urls.append(search_url)
		except Exception as e:
			print e
	return search_urls
def scrapeGuidesContent(links):
	# loop through all of the links
	for search_url in links:
		# set the values for the scraper
		page_link = search_url.url #'https://www.bls.gov/emp/ep_table_101.htm'
		page_title = search_url.title
		# initialize the scraper
		scrapetext = TextScraper(page_link, None, None)
		# run the scraper
		tag = "'div', 'class' : 'step-one-title stepright back-none1'"
		scrapetext.setHeadersText(tag, 'p')
		scrapetext.scrapeArea('inner-ac-block mrgNbtm')
		print scrapetext.data_text
		raise ValueError("Testing")
if __name__ == '__main__':
	# run the text scrapers
	scrapeOccupationSummaries()
	# links = scrapeGuidesLinks()
	# scrapeGuidesContent(links)