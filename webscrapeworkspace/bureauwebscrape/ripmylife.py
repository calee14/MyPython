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
import urllib
import urllib2 

# make program look like a browser, user_agent
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }
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
				search_urls.append(blslink)
# set the url we want to scrape
search_url = search_urls[9]

class TableScraper(object):

	def __init__(self, search_url, html, classIdentifier, idName, linkFileName=None, dataFileName=None):
		# initialize variables
		self.url = None
		self.soup = None
		# grab html page source
		if html is None:
			page = None
			# set url
			self.url = ''+search_url+''
			# open the url
			page = urllib.urlopen(self.url)
			# get our soup
			self.soup = BeautifulSoup(page, 'html.parser')
		else:
			# run BeautifulSoup on the html
			self.soup = BeautifulSoup(html, 'html.parser')
		# set request objects to hold indexes
		self.requests_objects = []
		# class or id of the table
		self.classIdentifier = classIdentifier
		# class or id name of the table
		self.idName = idName
		# file names
		self.linkFileName = linkFileName
		self.dataFileName = dataFileName
		
	def findHead(self, tablehtml):
		head = tablehtml.find('thead').find('tr')
		return head
	def getColumns(self, tablehead):
		columns = []
		for head in tablehead:
			if isinstance(head, NavigableString):
				# print 'we found a navigablestring'
				continue
			else:
				columns.append(head)
		return columns
	def getColumnNames(self, tablecolumns):
		# set a list to take in the names of each colomn
		columnNames = []
		# loop through the colomn heads
		for i in range(len(tablecolumns)):
			# get the text of the colmns
			columnNames.append(tablecolumns[i].findAll(text=True))
		# return the list of names
		return columnNames
	def createHeaders(self, tablehead, columnNames):
		# print len([head for head in tablehead])
		header_list = []
		temp_list = []
		for i in range(len(tablehead)):
			colspan = 0
			try:
				colspan = int(tablehead[i]['colspan'])
			except Exception as e:
				colspan = 1
			# print tablehead[i]['colspan']
			title = columnNames[i]
			# print columnNames[i]
			header = TableHeader(colspan, title, i)
			header_list.append(header)
			rangeOfRequests = header.findIndexes(None, None, lastList=temp_list)
			temp_list.append(rangeOfRequests)
			# print rangeOfRequests
		# print count
		self.requests_objects = temp_list
		return header_list

	def scrapeHeader(self, classIdentifier, idName):
		# print 'intheheader'
		# scrape the header of table
		# find table
		table = self.soup.find('table', attrs={''+classIdentifier+'' : ''+idName+''}) 
		# print table
		head = self.findHead(table)
		# print head
		columns = self.getColumns(head)
		# print columns
		names = self.getColumnNames(columns)
		# print names
		headers = self.createHeaders(columns, names)
		# print self.requests_objects
		# raise error
		# print [header.title for header in headers]
		
		# # loop through each row
		# count = 0
		# # list to hold headers
		# header_list = []
		# # get the headers
		# for head in header:
		# 	try:
		# 		title = ''
		# 		if noHeader is False:
		# 			try:
		# 				# get title of header
		# 				title = head.text.encode('utf-8')
		# 			except:
		# 				# move on to the next loop if we can't find the title
		# 				continue
		# 		# set length of array
		# 		colspan = 0
		# 		# try to find length
		# 		try:
		# 			colspan = int(head.get('colspan'))
		# 		except:
		# 			# if we can find it set it to one
		# 			colspan = 1
		# 		# set an array
		# 		array = []
		# 		for header in header_list:
		# 			array.append(header.requests_objects)
		# 		header = TableHeader(colspan, title, count, array)
		# 		self.requests_objects.append(header.findIndexes())
		# 		count += 1
		# 		# print str(header.requests_objects) + 'hi this is the objects'
		# 		header_list.append(header)
		# 	except Exception as e:
		# 		print e
		return headers

	def init_list_of_objects(self, size):
	    list_of_objects = list()
	    for i in range(0,size):
	        list_of_objects.append( list() ) # different object reference each time
	    return list_of_objects

	def findContent(self, table):
		rows = table.find('tbody').find_all('tr')
		return rows
	def cleanArrays(self, array):
		for i in range(len(array)):
			array[i] = array[i].strip()
		return array
	def getContentInEachRow(self, rows):
		content_list = []
		# loop through each row in table
		for i in range(len(rows)):
			data_list = []
			# print rows[i]
			# loop through each data cell
			for data in rows[i]:
				if isinstance(data, NavigableString):
					# print 'we found a navigablestring'
					continue
				# print data
				text = data.findAll(text=True)
				text = self.cleanArrays(text)
				data_list.append(text)
				# print text
			content_list.append(data_list)
		return content_list
	def organizeContent(self, content):
		organized = self.init_list_of_objects(len(self.requests_objects))
		for row in content:
			for i in range(len(self.requests_objects)):
				append_list = []
				for num in self.requests_objects[i]:
					append_list.append(row[num])
				organized[i].append(append_list)
		return organized
	def scrapeContent(self, header_list, classIdentifier, idName):
		table = self.soup.find('table', attrs={''+classIdentifier+'' : ''+idName+''}) 
		rows = self.findContent(table)
		# print rows
		content = self.getContentInEachRow(rows)
		# print content
		organizedContent = self.organizeContent(content)
		# print organizedContent
		# # find table
		# table = self.soup.find('table', attrs={''+classIdentifier+'' : ''+idName+''})
		# if table is None:
		# 	table = self.soup
		# else:
		# 	pass
		# # scrape the contents of the header
		# contents = table.find('tbody')
		# rows = contents.find_all('tr')
		# num_rows = 0
		# # return array
		# return_array = self.init_list_of_objects(len(self.requests_objects))
		# for row in rows:
		# 	num_rows += 1
		# 	# array to store all of our data
		# 	children = []
		# 	# for item in row:
		# 	items = row.find_all('td')
		# 	print items[0].nextSibling
		# 	# recursive loop to find a element with text
		# 	for item in items:
		# 		print str(len(items)) + "this"
		# 		nextNode = item
		# 		while True:
		# 			# get he next 
		# 			nextNode = nextNode.findNext()
		# 			try:
		# 				# try getting a text attribute 
		# 				nextNode.text
		# 			except AttributeError:
		# 				# if there is a error
		# 				pass
		# 			else:
		# 				# if we found the text
		# 				children.append(nextNode)
		# 				break
		# 		print len(children)
		# 	# set count s
		# 	print str(children) + 'sparta'
		# 	print str(num_rows) + "rows"
		# 	count = 0
		# 	# after appending them to children we add to return array
		# 	for num_array in self.requests_objects:
		# 		append_array = []
		# 		for num in num_array:
		# 			print str(num) + 'num'
		# 			try:
		# 				append_array.append(str(children[num].text.encode('utf-8')).strip())
		# 			except Exception as e:
		# 				print e
		# 				print 'we could not fit it in header_list'
		# 		return_array[count].append(append_array)
		# 		count += 1
		# 	print return_array
		return organizedContent
	def checkLenOfArrays(self, arrays):
		for i in range(len(arrays)):
			for j in range(i + 1, len(arrays)):
				if len(arrays[i].children) != len(arrays[i].children):
					raise ValueError('Represents a hidden bug, do not catch this')
		# it doesn't matter which array we get because they're all the same length
		return len(arrays[0].children)
	def combineArrays(self, arrays):
		# print "incombinearrays"
		# create a variable of the length of the arrays
		length_of_all_arrays = self.checkLenOfArrays(arrays)
		# set an empty array of slots for future functions
		occupations = self.init_list_of_objects(length_of_all_arrays) #[None] * len(header_list[0].children)  # Create list of 100 'None's
		# print str(len(occupations)) + " length"
		# check if we have the same amount
		# print str(len(arrays)) + ' len of arrays'
		for array in arrays:
			count = 0 
			# print len(array.children)
			for child in array.children:
				# print str(count) + "count"
				child_index = array.children.index(child)
				# print str(child_index) + 'index'
				occupations[count].append(child)
				count += 1
		# for array in arrays:
			# print str(array.children) + array.title
			# print len(array.children)
		# print len(occupations)
		# for occupation in occupations:
			# print occupation
		# print str(occupations[9]) + 'hi'
		return arrays, occupations

	def getLinks(self, classIdentifier, idName):
		# find table
		table = self.soup.find('table', attrs={''+classIdentifier+'' : ''+idName+''})
		if table is None:
			table = self.soup
		else:
			pass
		# scrape the contents of the header
		contents = table.find('tbody')
		link_header = contents.find_all('h4')
		# list of all the occupations
		occupation_links = []
		for header in link_header:
			# get a element which contains the link
			atag = header.find('a')
			link = atag['href']
			# get the title
			title = atag.text
			# create the blslink object
			blslink = BLSLink(self.url, link)
			# add title
			blslink.addChild(title)
			# append object to the array
			occupation_links.append(blslink)
		return occupation_links
	def flatten(self, lst):
	    if not lst:
	        return []
	    elif not isinstance(lst, list):
	        return [lst] 
	    else:
	        return self.flatten(lst[0]) + self.flatten(lst[1:])
	def addToDatabase(self, values):
		databasemaster = databasecreator()
		value_list = []
		for i in range(len(values)):
			values[i] = self.flatten(values[i])
		# databasemaster.addToTable() TODO: work on adding to database
	def jsonData(self, header_list=None, occupations=None):
		# print 'injsondata'
		json_occupations_data = []
		json_links_data = []
		# write it to a json file
		for occupation in occupations:
			json_array = []
			for header in header_list:
				json_data = {
					header.title : occupation[header_list.index(header)]
				}
				json_array.append(json_data)
			json_occupations_data.append(json_array)

		# write links to a json file
		links = self.getLinks(self.classIdentifier, self.idName)
		for link in links:
			json_links_data.append(link.createjson())
		# print json_occupations_data
		return json_occupations_data, json_links_data

	def writeToJSON(self, array):
		for data in array:
			filename = ''+data.file+''
			f = open(filename, "w")
			jsonstuff = json.dumps(data.data, indent=4)
			f.write(jsonstuff)

	def scrape(self):
		headers = self.scrapeHeader(self.classIdentifier, self.idName)
		contents = self.scrapeContent(headers, self.classIdentifier, self.idName)
		count = 0
		for content in contents:
			headers[count].addChild(content)
			count += 1
		header_list, occupations = self.combineArrays(headers)
		self.addToDatabase(occupations)
		# json_occupations_data, json_links_data = self.jsonData(header_list, occupations)
		# print str(json_occupations_data) + "hi and stuff"
		# BLSData = namedtuple('BLSData', 'data file')
		# content1 = BLSData(json_occupations_data, self.dataFileName)
		# content2 = BLSData(json_links_data, self.linkFileName)
		# return [content1, content2]
			
page_link = 'https://www.bls.gov/emp/ep_table_101.htm'
classIdentifier = 'class'
idName = 'regular'
linkFileName = 'occupationlinks.json'
dataFileName = 'occupations.json'
# run it 
retriever = TableScraper(page_link, None, classIdentifier, idName, linkFileName, dataFileName)
retriever.scrape()
# data = retriever.scrape()
# retriever.writeToJSON(data)

