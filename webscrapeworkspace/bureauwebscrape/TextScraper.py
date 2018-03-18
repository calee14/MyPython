# import libraries for table scraper
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import Tag, NavigableString, BeautifulSoup
from collections import namedtuple
from BLSContent import BLSContent
import json
import sys
# directory for where our database code is
sys.path.append('/Users/cap1/beginningpython/pythondatabases')
from databaseeptable import DatabaseCreator
from databasedata import DatabaseData
import urllib
import urllib2

class TextScraper(object):

	def __init__(self, search_url, linkFileName=None, dataFileName=None):
		self.url = '%s' % (search_url)
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
		req = urllib2.Request(self.url, headers=hdr)
		# open the url
		page = urllib2.urlopen(req)
		# get our soup
		self.soup = BeautifulSoup(page, 'html.parser')
		self.data_text = []
		self.linkFileName = linkFileName
		self.dataFileName = dataFileName
	def setHeadersText(self, headers, text):
		self.header_tag = headers
		self.text_tag = text
	# NOTES
	# New Method to scrape texts:
	# Scrape all divs within a specific div or element
	# Iterate through all of the elements in the specified elements
	# Use the getAll() function to get texts in arrays.
	# After the text is in the array seperate them from titles and text
	# We can tell if they're title by sentence length(2-), word count(count number of spaces, 9-), char count (49-)
	# We can tell if they're text by sentence length (3+), word count (count number of spaces, 10+), char count (50+)
	# Repeat this step until we've scraped all sections
	# New Method to scrape texts:
	# Scrape all divs within a specific div or element
	# Iterate through all of the elements in the specified elements
	# Use the find methods to find the header tag
	# Use the find_all method to find all of the text tags
	def scrapeArea(self, element_type):
		element_tag = self.soup.find("div", {"id": "%s" % (element_type)})
		for element in element_tag:
			if element.name == self.header_tag:
				title = element.getText()
				# print title 
				container = BLSContent(title)
				self.data_text.append(container)
			if element.name == self.text_tag:
				text = element.getText()
				# print text
				self.data_text[-1].addChild(text)
	def flatten(self, lst):
	    if not lst:
	        return []
	    elif not isinstance(lst, list):
	        return [lst] 
	    else:
	        return self.flatten(lst[0]) + self.flatten(lst[1:])
	def checkString(self, string):
		string = ' '.join(string.split())
		for ch in string:
			if ch.isdigit():
				string = string[1:] + ch
			else:
				break
		for ch in [',', '-', '(', ')']:
			if ch in string:
				string = string.replace(ch, '')
		return string.strip().replace(" ", "_")
	def addToDatabase(self, ctitle, column_headers, tabletitle):
		# initialize our database creators
		databasemaster = DatabaseCreator()
		value_list = DatabaseData()
		# set our titles
		TitleTuple = namedtuple('TitleTuple', 'title datatype')
		# create of containers
		title_list = []
		for title in column_headers:
			titleText = TitleTuple(self.checkString(title), "VARCHAR(1000)")
			title_list.append(titleText)

		text_list = [" ".join(child.text) for child in self.data_text]
		text_list = [text.encode('utf-8') for text in text_list]
		text_list.insert(0, ctitle.encode('utf-8'))
		text_list = text_list[:len(title_list)]
		# # add our text to our 
		# for child in self.data_text:
		# 	print child.text
		# 	text_list = []
		# 	text_list.append(child.title)
		# 	text_list.append(" ".join(child.text))
		# 	text_list = [text.encode('utf-8') for text in text_list]
		value_list.addrow(text_list)
		# add title list
		value_list.addheadertitle(title_list)
		# create and update db table
		databasemaster.createTable(value_list, self.checkString(tabletitle))
		databasemaster.addToTable(value_list, self.checkString(tabletitle))
	def dropTableInDatabase(self, dbtitle):
		databasemaster = DatabaseCreator()
		databasemaster.dropTable(self.checkString(dbtitle))
	def check(self):
		data_text = self.data_text
		for text in data_text:
			print text.title
			print text.children


