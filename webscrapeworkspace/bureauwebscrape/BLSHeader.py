class HeaderOccupation(object):

	def __init__(self, num_children, title, index, array):
		self.num_children = num_children
		self.index = int(index)
		self.requests_objects = self.findIndexes(index, num_children, array)
		self.title = title
		self.children = []

	def addChild(self, child):
		self.children.append(child)

	def findIndexes(self, index, num_children, array):
		num_range = []
		if index > 0:
			lastObjectIndex = index - 1
			lastObject = array[lastObjectIndex]
			return_array = []
			for num in lastObject:
				new_num = num + 2
				return_array.append(int(new_num))
			return return_array[:num_children]
		else: 
			return range(index, index + num_children)
		return 