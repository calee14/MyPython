from TableScraper import TableScraper
import json
from collections import namedtuple

# make program look like a browser, user_agent
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

def flatten(lst):
	# flatten function to get all values the the array no matter where they are
	# flatten gets all values into one array
    if not lst:
        return []
    elif not isinstance(lst, list):
        return [lst] 
    else:
        return flatten(lst[0]) + flatten(lst[1:])

def scrape_main_table():
	# function scrapes the major occupation groups
	# scrape the main occupations table
	# get values for the scraper 
	page_link = 'https://www.bls.gov/emp/ep_table_101.htm'
	page_title = 'MajorOccupations'
	classIdentifier = 'class'
	idName = 'regular'
	linkFileName = None#'occupationlinks.json'
	dataFileName = None#'occupations.json'
	# create scraper, run it 
	retriever = TableScraper(page_link, page_title, classIdentifier, idName, linkFileName, dataFileName)
	retriever.scrape()

def scrape_ooh_table():
	# scraopes the careers in the major occupation groups
	# scrape the bls.gov/ooh tables
	# search keys
	search_urls = []
	# get json file name 
	jsonfilename = "links.json"
	# open json file as var json_data
	with open(jsonfilename) as json_data:
		# store it in variable d
		d = json.load(json_data)
		# get get the object title and url
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
	# set values for the text file
	linkFileName = 'occupationlinks.json'
	dataFileName = 'occupations.json'
	# clear the json files because we are adding to it
	f = open(linkFileName, 'w').close()
	f = open(dataFileName, 'w').close()
	# links we get from the scraping
	links = []
	for search_url in search_urls:
		# set the values for the scraper
		page_link = search_url.url #'https://www.bls.gov/emp/ep_table_101.htm'
		page_title = search_url.title
		classIdentifier = 'class'
		idName = 'display'
		# run it 
		# try is temporary for testing purposes
		try:
			retriever = TableScraper(page_link, page_title, classIdentifier, idName, linkFileName, dataFileName)
			scrapedLinks = retriever.scrape()
			links.append(scrapedLinks)
		except Exception as e:
			print e
	# sorry for the language
	# add the links and titles to the text file
	scrapedata = [data.data for data in links]
	finaldata = flatten(scrapedata)
	f = open('occupationlinks.json', "a")
	jsonstuff = json.dumps(finaldata, indent=4)
	f.write(jsonstuff)

def scrape_careers():
	# scrape the summary of the data of the careers
	# scrape the bls.gov/ooh tables
	# search keys
	search_urls = []
	# get json file name 
	jsonfilename = "occupationlinks.json"
	# open json file as var json_data
	with open(jsonfilename) as json_data:
		# store it in variable d
		d = json.load(json_data)
		print d
		# get the title and url of the object
		for link in d:
			for child in link:
				title = link[child]
				for url in title:
					blslink = title[url]
					SearchUrl = namedtuple('SearchUrl', 'title url')
					searchData = SearchUrl(child, blslink)
					search_urls.append(searchData)
	# loop through all of the urls
	for search_url in search_urls:
		# set the data for the scraper
		page_link = search_url.url #'https://www.bls.gov/emp/ep_table_101.htm'
		page_title = search_url.title
		table_title = "statsummaries"
		classIdentifier = 'id'
		idName = 'quickfacts'
		linkFileName = None #'occupationlinks.json'
		dataFileName = None #'occupations.json'
		headers = ["title", "quickfacts1", "quickfacts2"]
		# run it 
		retriever = TableScraper(page_link, page_title, table_title, classIdentifier, idName, headers, linkFileName, dataFileName)
		retriever.scrape()

if __name__ == '__main__':
	# run the functions
	# scrape_main_table()
	# scrape_ooh_table() 
	scrape_careers()
