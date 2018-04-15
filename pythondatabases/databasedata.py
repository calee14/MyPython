class DatabaseData(object):
	def __init__(self):
		# initialize the lists
		self.data_list = []
		self.column_list = []
	def addrow(self, values):
		# add a row to the datalist variables
		# row = list of data
		row = []
		# run checks on the data and add to the lists
		for value in values:
			print value
			if self.checkdata(value):
				# if the check is good
				row.append(value)
			else:
				raise ValueError('Object was given wrong data') 
		self.data_list.append(row)
	def addheadertitle(self, values):
		# add the header titles to the column list variables
		titles = []
		# for header title in the list check them then add to the list
		for value in values:
			if self.checkdata(value):
				titles.append(value)
			else:
				raise ValueError('Object was given wrong data')
		self.column_list = titles
	def checkdata(self, value):
		# function to check the value we are adding
		# NOTE: function might be useless potentially; might remove in the future
		if isinstance(value, tuple):
			if all(value):
				return True
		elif isinstance(value, str):
			return True
		elif isinstance(value, list):
			return True
		else:
			return False

