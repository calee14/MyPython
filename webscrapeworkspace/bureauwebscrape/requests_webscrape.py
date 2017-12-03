import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.yellowpages.com/los-angles-ca/coffee?g=los%20angles%2C%20ca&q=coffee")
soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")

for link in links:
	if "http" in link:
		print("<a href='%s'>%s</a>") %(link.get("href"), link.text)

g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
	print(item.contents[0].find_all("a", {"class": "business-name"})[0].text)
	# print street adress
	try:
		print(item.contents[1].find_all("span", {"itemprop" : "streetAddress"})[0].text)
	except:
		pass
	# print address locality
	try: 
		print(item.contents[1].find_all("span", {"itemprop" : "addressLocality"})[0].text.replace(',', ''))
	except:
		pass
	# print address region
	try:
		print(item.contents[1].find_all("span", {"itemprop" : "addressRegion"})[0].text)
	except:
		pass
	# print postal code
	try:
		print(item.contents[1].find_all("span", {"itemprop" : "postalCode"})[0].text)
	except:
		pass
	# print primary
	try:
		print(item.contents[1].find_all("div", {"class" : "primary"})[0].text)
	except:
		pass