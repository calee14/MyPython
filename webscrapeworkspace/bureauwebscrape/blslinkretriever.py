from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from BLSHeader import HeaderOccupation
import json
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

# get webdriver and call phantomjs
driver = webdriver.PhantomJS()
driver.get(''+search_urls[9]+'')

# waiting for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "wrapper-outer")))
link = driver.find_element_by_css_selector(".sorting")
link.click()
html = driver.page_source

class TableRetriever(object):

	def __init__(self, search_urls, html):
		# set url
		# self.url = ''+search_urls[5]+''
		# open the url
		# self.page = urllib.urlopen(self.url)
		# run BeautifulSoup on the html
		self.soup = BeautifulSoup(html, 'html.parser')
		self.requests_objects = []

	def scrapeHeader(self):
		# scrape the header of table
		# find table
		table = self.soup.find('table', attrs={'id' : 'landing-page-table'})
		# find header
		header = table.find('thead').find('tr')
		# loop through each row
		count = 0
		# list to hold headers
		header_list = []
		# get the headers
		for head in header:
			try:
				# get title of header
				title = head.text.encode('utf-8')
				# set length of array
				colspan = 0
				# try to find length
				try:
					colspan = int(head['colspan'])
				except:
					# if we can find it set it to one
					colspan = 1
				# set an array
				array = []
				for header in header_list:
					array.append(header.requests_objects)
				header = HeaderOccupation(colspan, title, count, array)
				self.requests_objects.append(header.findIndexes())
				count += 1
				print header.requests_objects
				header_list.append(header)
			except Exception as e:
				# print e
				pass
		return header_list

	def init_list_of_objects(self, size):
	    list_of_objects = list()
	    for i in range(0,size):
	        list_of_objects.append( list() ) # different object reference each time
	    return list_of_objects

	def scrapeContent(self, header_list):
		# find table
		table = self.soup.find('table', attrs={'id' : 'landing-page-table'})
		# scrape the contents of the header
		contents = table.find('tbody')
		rows = contents.find_all('tr')
		num_rows = 0
		# return array
		return_array = self.init_list_of_objects(len(self.requests_objects))
		for row in rows:
			num_rows += 1
			# array to store all of our data
			children = []
			# for item in row:
			items = row.find_all('td')
			print items[0].nextSibling
			for item in items:
				print str(len(items)) + "this"
				nextNode = item
				while True:
					# get he next 
					nextNode = nextNode.findNext()
					try:
						# try getting a text attribute 
						nextNode.text
					except AttributeError:
						# if there is a error
						pass
					else:
						# if we found the text
						children.append(nextNode)
						break
				print len(children)
			# else:
			print str(children) + 'sparta'
			print str(num_rows) + "rows"
			count = 0
			# after appending them to children we add to return array
			for num_array in self.requests_objects:
				append_array = []
				for num in num_array:
					print str(num) + 'num'
					append_array.append(str(children[num].text.encode('utf-8')))
				return_array[count].append(append_array)
				count += 1
			print return_array
		return return_array

	def combineArrays(self, arrays):
		length_of_all_arrays = 0
		for array in arrays:
			for array2 in arrays:
				try:
					length_of_all_arrays = len(array.children)
					len(array.children) == len(array2.children)
					print("okay")
				except Exception as e:
					print e
		occupations = self.init_list_of_objects(length_of_all_arrays) #[None] * len(header_list[0].children)  # Create list of 100 'None's
		print str(len(occupations)) + " length"
		# check if we have the same amount
		print str(len(arrays)) + ' len of arrays'
		for array in arrays:
			count = 0 
			for child in array.children:
				print str(count) + "count"
				child_index = array.children.index(child)
				print str(child_index) + 'index'
				occupations[count].append(child)
				count += 1
		for array in arrays:
			print str(array.children) + array.title
			print len(array.children)
		print len(occupations)
		for occupation in occupations:
			print occupation
		# print str(occupations[9]) + 'hi'
		return arrays, occupations

	def jsonData(self, header_list, occupations):
		# write it to a json file
		json_occupations_data = []
		for occupation in occupations:
			json_array = []
			for header in header_list:
				json_data = {
					header.title : occupation[header_list.index(header)]
				}
				json_array.append(json_data)
			json_occupations_data.append(json_array)

		# write it in json file
		filename = "occupations.json"
		f = open(filename, "w")
		jsonstuff = json.dumps(json_occupations_data, indent=4)
		f.write(jsonstuff)

	def scrape(self):
		headers = self.scrapeHeader()
		contents = self.scrapeContent(headers)
		count = 0
		for content in contents:
			headers[count].addChild(content)
			count += 1
		header_list, occupations = self.combineArrays(headers)
		self.jsonData(header_list, occupations)
		print self.requests_objects
# run it 
retriever = TableRetriever(search_urls, html)
retriever.scrape()

# filename = "test.txt"
# f = open(filename, "w")

# content = driver.find_element_by_css_selector('.gsc-wrapper')
# search_results = content.find_elements_by_css_selector('.gsc-webResult .gsc-result')
# title_list = []
# for result in search_results:
# 	title = result.find_element_by_css_selector('a.gs-title')
# 	title_list.append(title)
# for result in title_list:
# 	title = result.text
# 	link = result.get_attribute('href')
# 	print(link)
	#print title

# results = expansion.find_elements_by_css_selector(".gsc-result")
# for result in results:
# 	f.write("class attribute: " + result.get_attribute('class'))
# 	print(result.get_attribute("class"))

# for comparison in driver.find_elements_by_css_selector(".gsc-expansionArea"):
#     # description = comparison.find_element_by_css_selector(".gsc-result")
#     f.write("class attribute: " + comparison.get_attribute('class'))
#     print(comparison.get_attribute("class"))
######################### driver end ######################
# driver.close()
