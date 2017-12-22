# import libraries
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import json
from BLSHeader import HeaderOccupation

# make program look like a browser, user_agent
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

# set url
url = "https://www.bls.gov/emp/ep_table_101.htm"
# open the url
page = urllib.urlopen(url)
# run BeautifulSoup on the html
soup = BeautifulSoup(page, 'html.parser')
# find table
table = soup.find('table', attrs={'class' : 'regular'})
# find header
header = table.find('thead').find('tr')
# scrape the header of table
# list
header_list = []
# loop through each row
count = 0
# get the headers
for head in header:
	try:
		title = head.find('strong').text.encode('utf-8')
		colspan = int(head['colspan'])
		header = ''
		array = []
		for header in header_list:
			array.append(header.requests_objects)
		header = HeaderOccupation(colspan, title, count, array)
		count += 1
		print str(header.requests_objects) + '123'
		header_list.append(header)
	except Exception as e:
		# print e
		pass
# scrape the contents of the header
contents = table.find('tbody')
for row in contents:
	children = []
	# for item in row:
	try:
		children = row.find_all('p')
		print children
	except Exception as e:
		# print e
		pass
	else:
		# if try is succuessful
		for header in header_list:
			append_array = []
			for num in header.requests_objects:
				append_array.append(str(children[num].text))
			header.addChild(append_array)

def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() ) #different object reference each time
    return list_of_objects

arrays = init_list_of_objects(23) #[None] * len(header_list[0].children)  # Create list of 100 'None's
print len(arrays) 
# check if we have the same amount
for header in header_list:
	try:
		for header2 in header_list:
			try:
				length_of_all_arrays = len(header.children)
				len(header.children) == len(header2.children)
				print("okay")
			except Exception as e:
				print e
	except Exception as e:
		print e
	else:
		for child in header.children:
			child_index = header.children.index(child)
			print child_index
			arrays[child_index].append(child)

print arrays[0]
json_occupations_data = []
for array in arrays:
	json_array = []
	for header in header_list:
		json_data = {
			header.title : array[header_list.index(header)]
		}
		json_array.append(json_data)
	json_occupations_data.append(json_array)

# write it in json file
filename = "careers.json"
f = open(filename, "w")
jsonstuff = json.dumps(json_occupations_data, indent=4)
f.write(jsonstuff)
# for header in header_list:
# 	for index in len(header.children):
# 		pass
filename = "test.txt"
f = open(filename, "w")
for header in header_list:
	for child in header.children:
		f.write(''+header.title+' '+str(child)+'\n')

	f.write(''+str(len(header.children))+' \n')
