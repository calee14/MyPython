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
			self.title = '-'.join(title).strip()
		# index of were we are in the header list
		if index is None:
			index = 0
		else:
			self.index = int(index)
		#self.requests_objects = self.findIndexes(self.index, self.num_children, self.array)
		self.children = []
	def flatten(self, lst):
		# get all values in the list into one list
	    if not lst:
	        return []
	    elif not isinstance(lst, list):
	        return [lst] 
	    else:
	        return self.flatten(lst[0]) + self.flatten(lst[1:])

	def addChild(self, child):
		# add a value scraped
		if isinstance(child, list):
			for c in child:
				self.children.append(c)
		else:
			self.children.append(child)
	# finds the indexes of the arrays for the objects
	def findIndexes(self, index=None, num_children=None, lastList=None):
		# no index then we use our own index
		# NOTES: don't know how that works or what I was thinking. Will fix issue soon
		if index is None:
			index = self.index
		# no number of properties: children then we use our own index
		# NOTES: don't know how that works or what I was thinking. Will fix issue soon
		if num_children is None:
			num_children = self.num_children
		if index > 0:
			# get the object of the last class, the one before this
			lastObjectList = lastList[-1]
			# print lastObjectList[-1]
			# set the request indexes of this class
			return_array = range(int(lastObjectList[-1]) + 1, int(lastObjectList[-1]) + num_children + 1)
			return return_array[-num_children:]
		else: 
			# if this is the first class then return the first indexes
			return range(index, index + num_children)
		return "Error, there was something wrong with getting the request indexes"
	def hasProperties(self):
		# function checks if children has any data at all
		if not self.flatten(self.children):
			# if this no data all
			return False
		# there are values in the list
		return True



