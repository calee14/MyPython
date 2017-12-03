from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# search keys
search_occupations = []
# get json file name 
jsonfilename = "careers.json"
# open json file as var json_data
with open(jsonfilename) as json_data:
	# store it in variable d
	d = json.load(json_data)
	# get second object
	data = d[1]
	# get the keys
	keys = data.keys()
	# append keys
	search_occupations.append(keys[0])

for key in search_occupations:
	key = key.replace(" ", "+")

# get webdriver and call phantomjs
driver = webdriver.PhantomJS()
driver.get('https://data.bls.gov/search/query/results?q='+search_occupations[0]+'')

# waiting for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".gsc-results")))

filename = "test.txt"
f = open(filename, "w")

content = driver.find_element_by_css_selector('.gsc-wrapper')
search_results = content.find_elements_by_css_selector('a.gs-title')
iterator = 0
for result in search_results:
	iterator += 1
	link = result.get_attribute('href')
	print(link)
	print(iterator)

# results = expansion.find_elements_by_css_selector(".gsc-result")
# for result in results:
# 	f.write("class attribute: " + result.get_attribute('class'))
# 	print(result.get_attribute("class"))

# for comparison in driver.find_elements_by_css_selector(".gsc-expansionArea"):
#     # description = comparison.find_element_by_css_selector(".gsc-result")
#     f.write("class attribute: " + comparison.get_attribute('class'))
#     print(comparison.get_attribute("class"))
driver.close()

# from bs4 import BeautifulSoup
# import urllib
# import requests
# import json

# url = 'https://data.bls.gov/search/query/ajax_page_update.js'
# data = {
# 'q' : 'Management occupations'
# }
# response = requests.post(url, data=data)
# print(response.json())
# # List with google queries I want to make
# desired_google_queries = ['Word' , 'lifdsst', 'yvou', 'should', 'load', 'from']

# for query in desired_google_queries:
#     # Constracting http query
#     url = 'https://data.bls.gov/search/query/results?q=Management%20occupations' # + query
#     # For avoid 403-error using User-Agent
#     req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
#     response = urllib2.urlopen( req )
#     html = response.read()
#     # Parsing response
#     soup = BeautifulSoup(html, 'html.parser')
#     # Extracting number of results
#     resultStats = soup.find(id="resInfo-0").string
#     print(resultStats)