class databaseData(object):
	def __init__(self):
		self.data_list = []
		self.column_list = []
	def addrow(self, values):
		row = []
		for value in values:
			if self.checkdata(value):
				# if the check is good
				row.append(value)
			else:
				raise ValueError('Object was given wrong data') 
		self.data_list.append(row)
	def addheadertitle(self, values):
		titles = []
		for value in values:
			if self.checkdata(value):
				titles.append(value)
			else:
				raise ValueError('Object was given wrong data')
		self.column_list = titles
	def checkdata(self, value):
		if isinstance(value, tuple):
			if all(value):
				return True
		elif isinstance(value, str):
			return True
		else:
			return False

