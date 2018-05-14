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
		# set the url
		self.url = '%s' % (search_url)
		# set headers to mask us from websites who blacklist bots
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	    # make the request to the website server
		req = urllib2.Request(self.url, headers=hdr)
		# open the url
		page = urllib2.urlopen(req)
		# get our soup
		self.soup = BeautifulSoup(page, 'html.parser')
		self.data_text = []
		# set the links 
		self.linkFileName = linkFileName
		self.dataFileName = dataFileName
	def flatten(self, lst):
		# flatten the list to get all values in the list in one list
	    if not lst:
	        return []
	    elif not isinstance(lst, list):
	        return [lst] 
	    else:
	        return self.flatten(lst[0]) + self.flatten(lst[1:])
	def setHeadersText(self, headers, text):
		# set tags of the all elements we want to scrape
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
	# New Method to scrape texts:
	# We need something new
	def getArea(self, element, children=False, indexes=None):
		area = self.soup.find('div', {'id':'%s' % (element)})
		if children is True:
			if indexes is None:
				child_elements = []
				for child in area:
					if isinstance(child, NavigableString):
						continue
					else:
						child_elements.append(child)
				return child_elements
			elif len(indexes) >= 1:
				child_elements = []
				index = 0
				for child in area:
					if isinstance(child, NavigableString):
						continue
					else:
						if index in indexes:
							child_elements.append(child)
						index += 1
				return child_elements
		return -1
	def scrapeHTML(self, html_snippet, element_area):
		area = html_snippet.find(element_area)
		for element in area:
			if element.name == self.header_tag:
				title = element.getText()
				container = BLSContent(title)
				self.data_text.append(container)
			if element.name == self.text_tag:
				text = element.find_all(text=True)
				try:
					self.data_text[-1].addListChild(text)	
				except Exception as e:
					print e	
	def scrapeArea(self, element_type):
		# scrapes the specified area and stores it in the data_list variable
		# NOTES: need to change function to make more dynamic and useable
		# find the element area we want to scrape
		print self.soup
		element_tag = self.soup.select('div[style="display:block"]')
		print element_tag
		# loop through the elements of the element
		for element in element_tag:
			# if the element is the header
			if element.name == self.header_tag:
				# create a new BLSContent container
				title = element.getText()
				# print title 
				# make the container
				container = BLSContent(title)
				# add the container to the data_text list
				self.data_text.append(container)
			# the element is the text element
			if element.name == self.text_tag:
				# add the text to latest BLSContent container
				text = element.getText()
				# print text
				# add it
				self.data_text[-1].addChild(text)

	def checkString(self, string):
		# check the string for anything that will create an error with the database
		string = ' '.join(string.split())
		# loop through the characters
		for ch in string:
			# move digit string to the back because the database can't accept stirngs with integers in the front
			if ch.isdigit():
				# move the char to the end
				string = string[1:] + ch
			else:
				break
		# remove any special characters
		# loop through the characters we want to remove
		for ch in [',', '-', '(', ')']:
			# if the character is in the string then remove it
			# NOTES: put the condition in a while loop so we can keep removing the special characters until there are no more
			if ch in string:
				# remove the character
				string = string.replace(ch, '')
		return string.strip().replace(" ", "_")
	def checkList(self, list_):
		return list_
	def checkData(self, data):
		if isinstance(data, list):
			return self.checkList(data)
		elif isinstance(data, str):
			return self.checkString(data)
		return -1
	def addToDatabase(self, ctitle, tabletitle, column_headers=None, datainlist=False):
		# add our scraped data to the database
		# initialize our database creators
		databasemaster = DatabaseCreator()
		# create a DatabaseData to hold the data we scraped
		value_list = DatabaseData()
		# set our titles
		TitleTuple = namedtuple('TitleTuple', 'title datatype')
		# create of containers
		title_list = []
		if column_headers is not None:
			# loop through the column titles
			for title in column_headers:
				# put it in a tuple so it can specify what type the variable is 
				titleText = TitleTuple(self.checkString(title), "VARCHAR(5000)")
				# add the tuple
				title_list.append(titleText)
		elif column_headers is None:
			temp_list = [container.title.encode('utf-8') for container in self.data_text]
			temp_list.insert(0, "job_title")
			for title in temp_list:
				titleText = TitleTuple(self.checkString(title), "VARCHAR(5000)")
				title_list.append(titleText)
		print title_list
		text_list = []
		if datainlist is False:
			# combine all of the arrays in variable: child so we only have one string/value at the index
			text_list = [" ".join(child.text) for child in self.data_text]
			# encode the text
			text_list = [text.encode('utf-8') for text in text_list]
			# insert the title in the the front of the list
			text_list.insert(0, ctitle.encode('utf-8'))
			# make sure the length of the list is no more than how many columns we have
			text_list = text_list[:len(title_list)]
		elif datainlist is True:
			# setting the data from the data we scraped
			text_list = [container for container in self.data_text]
			# looping throught the data and getting the text
			text_list = [text.text for text in text_list]
			titles = [container.title for container in self.data_text]
			for i in range(len(text_list)):
				print str(titles[i]).encode('utf-8') + 'deez'
				text_list[i].insert(0, str(titles[i]).encode('utf-8'))
			text_list.insert(0, ctitle.encode('utf-8'))
		# # add our text to our 
		# for child in self.data_text:
		# 	print child.text
		# 	text_list = []
		# 	text_list.append(child.title)
		# 	text_list.append(" ".join(child.text))
		# 	text_list = [text.encode('utf-8') for text in text_list]
		# add the list to the container
		value_list.addrow(text_list)
		# add title list
		value_list.addheadertitle(title_list)
		# create and update db table
		# create the table
		databasemaster.createTable(value_list, self.checkData(tabletitle))
		# update the table
		databasemaster.addToTable(value_list, self.checkData(tabletitle))
	def dropTableInDatabase(self, dbtitle):
		# function to drop a table 
		# create an instance of the DatabaseCreator
		databasemaster = DatabaseCreator()
		# run the drop table function
		databasemaster.dropTable(self.checkString(dbtitle))
	def check(self):
		# checks the data we have
		# prints them to anylize data
		data_text = self.data_text
		for text in data_text:
			print text.title
			print text.children


