# import libraries
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import json
from Occupations import Occupation

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
# find row
rows = table.find_all("tr")
# data
data = []
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

occupations = []
for array in data:
	try:
		occupation = Occupation(array)
		occupations.append(occupation.jsonData())
	except:
		pass

filename = "careers.json"
f = open(filename, "w")
jsonstuff = json.dumps(occupations, indent=4)
f.write(jsonstuff)

# loop through the occupations
# for occupation in data:
# 	# try encoding url
# 	try:
# 		# pass in the word into the search bar a.k.a create html form
# 		values = {'s' :  occupation[0].replace(" ", "+")}
# 		# urlencode the word
# 		data = urllib.urlencode(values)

# 		# makes the request/form  
# 		request = urllib2.Request("https://data.bls.gov/search/query/results", data, headers)
# 		# response
# 		response = urllib2.urlopen(request)
# 		# read the page
# 		the_page = response.read()
# 		# turn the page into html 
# 		soup = BeautifulSoup(the_page, 'html.parser')
# 		if occupation[0] == 'Management occupations':
# 			stuff = soup.find_all("div", attrs={'class' : 'gs-result'})
# 			print(data)
# 			print stuff
# 	except:
# 		pass

