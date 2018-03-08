# import libraries for table scraper
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import Tag, NavigableString, BeautifulSoup
from BLSHeader import TableHeader
from BLSLink import BLSLink
from collections import namedtuple
import json
import sys
# directory for where our database code is
sys.path.append('/Users/cap1/beginningpython/pythondatabases')
from databaseeptable import databasecreator
from databasedata import databaseData
import urllib
import urllib2

class TextScraper(object):

	def __init__(self, search_url, dbtitle, classidentifier, idName, linkFileName=None, dataFileName=None):
		self.url = '%s' % (search_url)
		# open the url
		page = urllib.urlopen(self.url)
		# get our soup
		self.soup = BeautifulSoup(page, 'html.parser')
