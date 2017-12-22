import urlparse

class BLSLink(object):

	def __init__(self):
		self.children = []

	def addChild(self, child):
		if isinstance(child, list):
			for c in child:
				self.children.append(c)
		else:
			self.children.append(child)

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

	def is_absolute(self, url):
		return bool(urlparse.urlparse(url).netloc)
