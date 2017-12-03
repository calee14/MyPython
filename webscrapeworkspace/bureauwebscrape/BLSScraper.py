# import libraries
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import json
from Occupations import Occupation

class BLSScraper(object):

	def __init__(self):
		# make program look like a browser, user_agent
		self.user_agent = 'Mozilla/5 (Solaris 10) Gecko'
		self.headers = { 'User-Agent' : self.user_agent }
		# set url
		self.url = "https://www.bls.gov/emp/ep_table_101.htm"
		# open the url
		self.page = urllib.urlopen(self.url)
		# run BeautifulSoup on the html
		self.soup = BeautifulSoup(self.page, 'html.parser')

	def scrapeTable(self):
		# data
		data = []
		# find table
		table = self.soup.find('table', attrs={'class' : 'regular'})
		# find row
		rows = table.find_all("tr")
		# loop through each row
		for row in rows:
			# data
			occupation = []
			# loop through each 'td'
			for item in row:
				# get all the data in item
				try: 
					occupation.append(item.text)
					pass
				except:
					pass
			data.append(occupation)
		return data

	def writeData(self, filename, data):
		occupations = []
		for array in data:
			try:
				occupation = Occupation(array)
				occupations.append(occupation.jsonData())
			except:
				pass

		filename = filename
		f = open(filename, "w")
		jsonstuff = json.dumps(occupations, indent=4)
		f.write(jsonstuff)
		return

	def scrape(self):
		scraped_table = self.scrapeTable()
		self.writeData('careers.json', scraped_table)



