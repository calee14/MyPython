# import libraries for table scraper
# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from bs4 import Tag, NavigableString, BeautifulSoup
from BLSHeader import TableHeader
from BLSLink import BLSLink
from collections import namedtuple
import json
import sys
# directory for where our database code is
sys.path.append('/Users/cap1/beginningpython/pythondatabases')
from databaseeptable import DatabaseCreator
from databasedata import DatabaseData
import urllib
import urllib2 

class TableScraper(object):

	def __init__(self, search_url, dbtitle, tabletitle, classIdentifier, idName, dbheaders=None, linkFileName=None, dataFileName=None):
		# initialize variables
		self.url = None
		self.soup = None
		# grab html page source
		# set url
		self.url = ''+search_url+''
		# open the url
		page = urllib.urlopen(self.url)
		# get our soup
		self.soup = BeautifulSoup(page, 'html.parser')
		# set request objects to hold indexes
		self.requests_objects = []
		# class or id of the table
		self.classIdentifier = classIdentifier
		# class or id name of the table
		self.idName = idName
		# file names
		self.linkFileName = linkFileName
		self.dataFileName = dataFileName
		self.dbtitle = dbtitle
		self.tabletitle = tabletitle
		self.headers = dbheaders
	def findHead(self, tablehtml):
		# find the head element of the table
		head = tablehtml.find('thead').find('tr')
		return head
	def getColumns(self, tablehead):
		# get the columns in the header
		columns = []
		# loop through each column and add it to the list
		for head in tablehead:
			if isinstance(head, NavigableString):
				# print 'we found a navigablestring'
				continue
			else:
				columns.append(head)
		return columns
	def getColumnNames(self, tablecolumns):
		# get the titile of the column
		# set a list to take in the names of each colomn
		columnNames = []
		# loop through the colomn heads
		for i in range(len(tablecolumns)):
			# get the text of the colmns
			columnNames.append(tablecolumns[i].findAll(text=True))
		# return the list of names
		return columnNames
	def createHeaders(self, tablehead, columnNames):
		# get the the headers and create the TableHeader classes to hold the data
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
		# combine all the functions to scrape the header of the table
		# print 'intheheader'
		# scrape the header of table
		# find table
		table = self.soup.find('table', attrs={''+classIdentifier+'' : ''+idName+''}) 
		# print table
		# find the header elements of the table
		head = self.findHead(table)
		# print head
		# loop through all the columns
		columns = self.getColumns(head)
		# print columns
		# get the names of the columns
		names = self.getColumnNames(columns)
		# print names
		# create the TableHeader classes with the names
		headers = self.createHeaders(columns, names)
		return headers

	def init_list_of_objects(self, size):
		# creates a x number of lists in a list and returns it
	    list_of_objects = list()
	    for i in range(0,size):
	        list_of_objects.append( list() ) # different object reference each time
	    return list_of_objects
	def findContent(self, table):
		# find the table
		rows = table.find('tbody').find_all('tr')
		return rows
	def cleanArrays(self, array):
		# remove spaces in the string in the list
		for i in range(len(array)):
			array[i] = array[i].strip()
		return array
	def getContentInEachRow(self, rows):
		# get the text in each row of the table
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
				# get all the text in the cell of the table
				text = data.findAll(text=True)
				text = [' '.join(text).strip()]
				if isinstance(text, list):
					print ' '.join(text).strip()
				text = self.cleanArrays(text)
				# add the text/row to the data_list
				data_list.append(text)
				# print text
			content_list.append(data_list)
		return content_list
	def organizeContent(self, content):
		# creates a list containing lists: amount equal to the length of the requests objects
		organized = self.init_list_of_objects(len(self.requests_objects))
		# loop through the content
		for row in content:
			# loop through the number of TableHeader classes
			for i in range(len(self.requests_objects)):
				append_list = []
				# loop through the request objects indexes
				for num in self.requests_objects[i]:
					# append the data to the right list
					append_list.append(row[num])
				# the append_list would go to the master list
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
		return organizedContent
	def checkLenOfArrays(self, arrays):
		# checks the len of all the arrays
		# makes sure they're all equal to each other
		for i in range(len(arrays)):
			for j in range(i + 1, len(arrays)):
				if len(arrays[i].children) != len(arrays[i].children):
					raise ValueError('Represents a hidden bug, do not catch this')
		# it doesn't matter which array we get because they're all the same length
		return len(arrays[0].children)
	def combineArrays(self, arrays):
		# combine the lists from all of the TableHeaders

		# print "incombinearrays"
		# create a variable of the length of the arrays
		length_of_all_arrays = self.checkLenOfArrays(arrays)
		# set an empty array of slots for future functions
		occupations = self.init_list_of_objects(length_of_all_arrays) #[None] * len(header_list[0].children)  # Create list of 100 'None's
		# print str(len(occupations)) + " length"
		# check if we have the same amount
		# print str(len(arrays)) + ' len of arrays'
		# loop through all the lists
		for array in arrays:
			count = 0 
			# print len(array.children)
			for child in array.children:
				# print str(count) + "count"
				# print str(child_index) + 'index'
				print child

				occupations[count].append(child)
				count += 1
		return arrays, occupations

	def getLinks(self, classIdentifier, idName):
		# function to ge the links of the table
		# NOTES: figure out which table
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
		# function to flatten a list
		# gets all values the list has and puts it in one list
	    if not lst:
	        return []
	    elif not isinstance(lst, list):
	        return [lst] 
	    else:
	        return self.flatten(lst[0]) + self.flatten(lst[1:])
	def checkString(self, string):
		# function to check the string for any special character 
		# used for the database 
		# NOTES: might not need any more for we're checking it in the DatabaseCreator class
		# make all spaces singlespaced
		string = ' '.join(string.split())
		# loop through all of the characters
		for ch in string:
			# if the charcter is a number
			if ch.isdigit():
				# move it to the back
				# NOTES: do this because the database can't accept numbers infront of the 
				string = string[1:] + ch
			else:
				break
		# remove the special characters in the string
		for ch in [',', '-', '(', ')']:
			if ch in string:
				string = string.replace(ch, '')
		return string.strip().replace(" ", "_")
	def addToDatabase(self, values, titles, dbtitle, tabletitle, headers=None):
		# dbtitle = "".join(dbtitle.split())
		# creates a DatabaseCreator instance which makes a table in the database
		databasemaster = DatabaseCreator()
		# data we use to pass in to the DatabaseCreator
		value_list = DatabaseData()
		titleList = []
		# loop through all of the titles function was given
		# NOTE: no longer using titles for we are hard coding column headers
		for i in range(len(headers)):
			# create instance of tuple
			TitleTuple = namedtuple('TitleTuple', 'title datatype')
			# make a tule to add to the list
			titleData = TitleTuple(self.checkString(headers[i].encode('utf-8')), "VARCHAR(555)")
			# add it
			titleList.append(titleData)
		# add the title list to the DatabaseData class
		value_list.addheadertitle(titleList)
		# loop through the values function was given
		for i in range(len(values)):
			# filter the list in variable values
			newValueList = filter(None, self.flatten(values[i]))
			print newValueList
			# make sure all the strings in the list are ecoded
			sqlDataList = [newValueList[j].encode('utf-8') for j in range(len(newValueList))]
			print sqlDataList
			sqlDataList.insert(0, self.checkString(dbtitle).encode('utf-8'))
			# we need to add the title of the database title
			# add a row of data to the Database Data
			# addrow function is equivlent to adding one row in the pgadmin table
			value_list.addrow(sqlDataList)
		# table name for our database
		tabletitle = "".join(tabletitle.split())
		# create the table
		databasemaster.createTable(value_list, tabletitle)
		# add our values to it
		databasemaster.addToTable(value_list, tabletitle)
		# databasemaster.addToTable(value_list) #TODO: work on adding to database
	def jsonData(self, header_list=None, occupations=None):
		# turns our data to json format 
		# function is specified for the BLSHeader and occupations variables
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
	# def writeToJSON(self, array):
		# for data in array:
		# 	print array
		# 	raise
		# 	filename = ''+data.file+''
		# 	f = open(filename, "a")
		# 	jsonstuff = json.dumps(data.data, indent=4)
		# 	f.write(jsonstuff)
	def addContentToContainers(self, contents, containers):
		# add the data scraped to the right BLSHeader class
		# add the data to the BLSHeader class
		count = 0
		for content in contents:
			# add the properties 
			containers[count].addChild(content)
			count += 1
		index = 0
		# the properties in the list are empty then remove it
		for container in containers:
			# runs the check for values
			if container.hasProperties() is False:
				# remove it
				del containers[index]
			index += 1
		return containers
	def findHeaderTitles(self, headerlist):
		# This function is trying to get the header name list working for the database
		# we are trying to get a unquie title for each column in the database
		titles = []
		# loop through the headers
		for i in range(len(headerlist)):
			# loop through the request obects to get indexes
			for j in range(len(self.requests_objects[i])):
				# add the title to the list
				# NOTES: we added j to the end of the string so that there won't be any duplacite titles
				titles.append(headerlist[i].title + "_" + str(j))
		return titles
	def scrape(self):
		# main scrape function 
		# get the headers
		headers = self.scrapeHeader(self.classIdentifier, self.idName)
		# scrape the content of table
		contents = self.scrapeContent(headers, self.classIdentifier, self.idName)
		# organize into headers and lists
		header_list, occupations = self.combineArrays(self.addContentToContainers(contents, headers))
		# add the data to the database
		self.addToDatabase(occupations, self.findHeaderTitles(headers), self.dbtitle, self.tabletitle, self.headers)
		# turn the data in to json format
		json_occupations_data, json_links_data = self.jsonData(header_list, occupations)
		print str(json_occupations_data) + "hi and stuff"
		# if we have link files inputed then we can add the data to the files
		if self.linkFileName is not None or self.dataFileName is not None:
			BLSData = namedtuple('BLSData', 'data file')
			# data = BLSData(json_occupations_data, self.dataFileName)
			links = BLSData(json_links_data, self.linkFileName)
			return links
			# self.writeToJSON([data, links])

# data = retriever.scrape()
# retriever.writeToJSON(data)

