class BLSContent(object):

	def __init__(self, title=None):
		self.children = []
		if title is None:
			self.title = 'Container'
		else:
			self.title = self.cleanContent(title)

	def addChild(self, child):
		# clean the strings before append
		cleanedContent = self.cleanContent(child)
		# add content to children
		self.children.append(cleanedContent)

	def cleanContent(self, item): 
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
		

