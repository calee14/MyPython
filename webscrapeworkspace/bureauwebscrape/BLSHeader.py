class TableHeader(object):

	def __init__(self, num_children=None, title=None, index=None):
		# amount of children we are recieving
		if num_children is None:
			self.num_children = 0
		else:
			self.num_children = num_children
		# name of occupation
		if title is None or not title:
			self.title = "Header"
		else:
			self.title = '-'.join(title)
		# index of were we are in the header list
		if index is None:
			index = 0
		else:
			self.index = int(index)
		#self.requests_objects = self.findIndexes(self.index, self.num_children, self.array)
		self.children = []

	def addChild(self, child):
		if isinstance(child, list):
			for c in child:
				self.children.append(c)
		else:
			self.children.append(child)
			
	# finds the indexes of the arrays for the objects
	def findIndexes(self, index=None, num_children=None, lastList=None):
		if index is None:
			index = self.index
		if num_children is None:
			num_children = self.num_children
		if index > 0:
			lastObjectList = lastList[-1]
			print lastObjectList[-1]
			return_array = range(int(lastObjectList[-1]) + 1, int(lastObjectList[-1]) + num_children + 1)
			return return_array[-num_children:]
		else: 
			return range(index, index + num_children)
		return "Error, there was something wrong with getting the request indexes"
