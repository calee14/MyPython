class HeaderOccupation(object):

	def __init__(self, num_children=None, title=None, index=None, array=None):
		# amount of children we are recieving
		if num_children is None:
			selfl.num_children = 0
		else:
			self.num_children = num_children
		# name of occupation
		if title is None:
			title = "Occupation"
		else:
			self.title = title
		# index of were we are in the header list
		if index is None:
			index = 0
		else:
			self.index = int(index)
		# headerlist array
		if array is None:
			array = []
		else:
			self.array = array
		self.requests_objects = self.findIndexes(self.index, self.num_children, self.array)
		self.children = []

	def addChild(self, child):
		self.children.append(child)

	# finds the indexes of the arrays for the objects
	def findIndexes(self, index=None, num_children=None, array=None):
		if index is None:
			index = self.index
		if num_children is None:
			num_children = self.num_children
		if array is None: 
			array = self.array
		num_range = []
		if index > 0:
			lastObjectIndex = index - 1
			lastObject = array[lastObjectIndex]
			return_array = []
			for num in lastObject:
				new_num = num + num_children
				return_array.append(int(new_num))
			return return_array[-num_children:]
		else: 
			return range(index, index + num_children)
		return 