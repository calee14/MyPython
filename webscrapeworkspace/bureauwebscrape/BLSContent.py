class BLSContent(object):

	def __init__(self, title=None):
		# create text list to hold the text we scraped
		self.text = []
		# set the title of the class
		if title is None:
			self.title = 'Container'
		else:
			self.title = self.cleanContent(title)
	def cleanContent(self, item): 
		# clean the content
		try:
			# remove leading and trailing spaces and substitute multiple white spaces with one
			cleanContent = " ".join(item.strip().split())
			# return new content
			return cleanContent
		except Exception as e:
			print e
			print 'we could not clean'
		# if all fail return what came in
		return item
	def addChild(self, child):
		# clean the strings before append
		cleanedContent = self.cleanContent(child)
		# add content to children
		self.text.append(cleanedContent)
	def addListChild(self, child):
		if isinstance(child, list):
			for c in child:
				self.text.append(c)
		else:
			self.text.append(child)
	
		

