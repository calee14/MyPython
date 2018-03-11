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

	def __init__(self, search_url, dbtitle, linkFileName=None, dataFileName=None):
		self.url = '%s' % (search_url)
		# open the url
		page = urllib.urlopen(self.url)
		# get our soup
		self.soup = BeautifulSoup(page, 'html.parser')
		self.dbtitle = dbtitle
		self.data_text = []
		self.linkFileName = linkFileName
		self.dataFileName = dataFileName
	def setHeadersText(self, headers, text):
		self.header_tag = headers
		self.text_tag = text
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
	def addToDatabase(self, dbtitle):
		databasemaster = databasecreator
		title_list = []
		text_list = []
		for child in self.children:
			TitleTuple = namedtuple('TitleTuple', 'title datatype')
			titleData = TitleTuple(self.checkString(chlid.title.encode('utf-8')), "VARCHAR(555)")
			title_list.append(titleData)
			text_list.append(child.text)
		databasemaster.createTable(title_list)
	def check(self):
		data_text = self.data_text
		for text in data_text:
			print text.title
			print text.children


