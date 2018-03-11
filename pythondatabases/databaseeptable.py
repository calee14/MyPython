import sys
import psycopg2
import re
from databasedata import DatabaseData

class DatabaseCreator(object):
	def __init__ (self):
		self.con = None
		self.cur = None
	def utf8len(self, s):
		try:
			return len(s.encode('utf-8'))
		except:
			return s
	def remove_char(self, hi, n):
		first_part = hi[:n]
		last_pasrt = hi[n+1:]
		return first_part + last_pasrt
	def cleanString(self, string):
		for ch in ['(', ')', ':']:
			count = 0
			for char in string:
				if char == ch:
					string = string[:count] + '\\' + string[count:]
					count += 1
				count+=1
		return ' '.join(string.split())
		# print string + "josh"
	def removeSpecialCharacters(self, string):
		for ch in [':', '-']:
			count = 0
			for char in string:
				if char == ch:
					string = self.remove_char(string, count)
				count += 1
		# do this if the size of string (measured in bytes) is larger than 63
		if len(string) > 63:
			# we try to shorten it 
			# if later cases show the string we input with missing characters we know that the string was too big
			print("The string was too large. Attempting to shorten it")
			string = string.replace('_', '')
		return string.replace(',','')
	def connectToDatabase(self):
		self.con = psycopg2.connect("host='localhost' dbname='careersearchdb' user='postgres' password='capsdatabase'")
		self.cur = self.con.cursor()
		print("Sucessfully connect to database.")
	def checkIfTableExists(self, dbtitle):
		self.cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (dbtitle,))
		condition = self.cur.fetchone()[0]
		return condition
	def createTable(self, value, dbtitle):
		dbtitle = self.removeSpecialCharacters(self.cleanString(dbtitle)).lower()
		columns = None
		if isinstance(value, DatabaseData):
			columns = value.column_list
		else:
			raise ValueError("Object was given the wrong data")
		# connect to the database
		self.connectToDatabase()
		# adding the table
		try:
			# con = psycopg2.connect("host='localhost' dbname='careersearchdb' user='postgres' password='capsdatabase'")
			# cur = con.cursor()
			# print("Sucessfully connect to database.")
			if self.checkIfTableExists(dbtitle) == True:
				self.cur.execute("DROP TABLE %s" % (dbtitle))
				self.cur.execute("CREATE TABLE %s();" % (dbtitle))
			else:
				self.cur.execute("CREATE TABLE %s();" % (dbtitle))
			for column in columns:
				self.cur.execute("ALTER TABLE %s ADD %s %s;"  % (dbtitle, self.removeSpecialCharacters(column.title), self.removeSpecialCharacters(column.datatype)))
				print(self.utf8len("Altering table " + "ALTER TABLE %s ADD %s %s;" % (dbtitle, self.removeSpecialCharacters(column.title), self.removeSpecialCharacters(column.datatype))))
			print("Successfully created table")
			self.con.commit()
		except psycopg2.DatabaseError, e:
			print("Something went wrong with the database.")
			print(e)
	def addToTable(self, value, dbtitle):
		dbtitle = self.removeSpecialCharacters(self.cleanString(dbtitle)).lower()
		data = []
		# loop through each row of values
		if isinstance(value, DatabaseData):
			data = value.data_list
		else:
			raise ValueError("Object was given the wrong data")
		self.connectToDatabase()
		try:
			for items in data:
				print items
				items = [self.cleanString(item) for item in items]
				copy_string = re.sub(r'([a-z])(?!$)', r'\1,', '%s' * len(items))
				final_string = re.sub(r'(?<=[.,])(?=[^\s])', r' ', copy_string)
				query_string = 'INSERT INTO %s VALUES (%s);' % (dbtitle, final_string)
				self.cur.execute(query_string, items)
			print("Sucessfully updated table")
			self.con.commit()
		except psycopg2.DatabaseError, e:
			print("Something went wrong when trying to add data to the table")
			print(e)