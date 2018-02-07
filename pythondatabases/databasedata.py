class databaseData(object):
	def __init__(self):
		self.data_list = []

	def addrow(self, values):
		row = []
		for value in values:
			if self.checkdata(value):
				# if the check is good
				row.append(value)
			else:
				raise ValueError('Object was given wrong data') 
		self.data_list.append(row)
	def checkdata(self, value):
		print value
		if isinstance(value, tuple):
			if value.data is not None and value.command is not None and value.title:
				return True
		else:
			return False