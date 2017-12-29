import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import json
from urlparse import urlparse

class BLSLink(object):

	def __init__(self, url, link):
		self.children = []
		self.addChild(self.makeLink(url, link))
		self.link = self.findLink()
	def addChild(self, child):
		if isinstance(child, list):
			for c in child:
				self.children.append(c)
		else:
			self.children.append(child)
	def findLink(self):
		link = ''
		for child in self.children:
			if self.is_absolute(child):
				link = child
			else:
				continue
		return link
		
	def createjson(self):
		blsurl = ''
		title = ''
		for child in self.children:
			if self.is_absolute(child):
				blsurl = child
			else:
				title = child.lstrip()
		jsondata = {
			title : {'url' : str(blsurl)}
		}
		return jsondata

	def makeLink(self, url, link):
		# parse the domain of the url
		parsed_uri = urlparse(url)
		# get the domain form the string link
		domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
		link = domain+link
		return link

	def is_absolute(self, url):
		return bool(urlparse(url).netloc)
