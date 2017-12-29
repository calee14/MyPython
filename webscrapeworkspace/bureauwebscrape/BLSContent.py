class BLSContent(object):

	def __init__(self, title=None):
		self.children = []
		if title is None:
			self.title = 'Container'
		else:
			self.title = title

	def addChild(self, child):
		self.children.append(child)
