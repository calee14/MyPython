import sys
import psycopg2
import re
from databasedata import DatabaseData

class DatabaseCreator(object):
	def __init__ (self):
		# initialize the connection to database
		self.con = None
		# initialize the cursor/query tool of the database
		self.cur = None
	def utf8len(self, s):
		# function returns the size (bytes) of the string
		# useful if we have a name that is too long for the database
		try:
			return len(s.encode('utf-8'))
		except:
			return s
	def remove_char(self, hi, n):
		# function that removes a char from the string
		# used for removing special characters in string
		first_part = hi[:n]
		last_pasrt = hi[n+1:]
		return first_part + last_pasrt
	def cleanString(self, string):
		# cleans the string of any special characters
		# database will give errors if special kinds of strings are entered in the query
		# loop through the characters we want to find
		for ch in ['(', ')', ':']:
			count = 0
			# loop through the characters of the string
			for char in string:
				# if we found the string remove it
				if char == ch:
					string = string[:count] + '\\' + string[count:]
					count += 1
				count+=1
		return ' '.join(string.split())
		# print string + "josh"
	def removeSpecialCharacters(self, string):
		# removes the string of any special characters
		# NOTE: similar ot the cleanString function; plan to make them into one
		# loop through the characters we want to find
		for ch in [':', '-']:
			count = 0
			# loop through the characters of the string
			for char in string:
				# remove the char if we find it
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
		# connect to the database
		self.con = psycopg2.connect("host='localhost' dbname='careersearchdb' user='postgres' password='capsdatabase'")
		# set our cursor for the query tool
		self.cur = self.con.cursor()
		print("Sucessfully connect to database.")
	def checkIfTableExists(self, dbtitle):
		# function that checks if the table already exists
		self.cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (dbtitle,))
		# if there is a first row then there is a table
		condition = self.cur.fetchone()[0]
		return condition
	def createTable(self, value, dbtitle, check=False):
		# creates a table in the database
		# check the table name for any special characters 
		dbtitle = self.removeSpecialCharacters(self.cleanString(dbtitle)).lower()
		# initialize a columns variable
		columns = None
		# get the column headers from the DatabaseData class
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
			# run conditions to check if the table exists
			if self.checkIfTableExists(dbtitle) == False:
				# if the table doesn't exist then make one
				self.cur.execute("CREATE TABLE %s();" % (dbtitle))
			check = False
			# run code if we want to update the table every time 
			if check == True:
				# clear the table and it's contents
				if self.checkIfTableExists(dbtitle) == True:
					# drop the table and create a empty one with the same name (replacing the table)
					self.cur.execute("DROP TABLE %s" % (dbtitle))
					self.cur.execute("CREATE TABLE %s();" % (dbtitle))
				else:
					self.cur.execute("CREATE TABLE %s();" % (dbtitle))
			# add the columns to the table
			for column in columns:
				# add the column
				self.cur.execute("ALTER TABLE %s ADD %s %s;"  % (dbtitle, self.removeSpecialCharacters(column.title), self.removeSpecialCharacters(column.datatype)))
				print(self.utf8len("Altering table " + "ALTER TABLE %s ADD %s %s;" % (dbtitle, self.removeSpecialCharacters(column.title), self.removeSpecialCharacters(column.datatype))))
			print("Successfully created table")
			# commit our changes to the database
			self.con.commit()
		except psycopg2.DatabaseError, e:
			print("Something went wrong with the database.")
			print(e)
	def createTableSecond(self, value, dbtitle, tabletitle):
		dbtitle = self.removeSpecialCharacters(self.cleanString(dbtitle)).lower()
		columns = None
		if isinstance(value, DatabaseData):
			columns = value.column_list
		else:
			raise ValueError("Object was given the wrong data")
		self.connectToDatabase()
		try:
			if self.checkIfTableExists(dbtitle) == False:
				self.cur.execute("CREATE TABLE %s();" % (tabletitle))
			for column in columns:
				self.cur.execute("ALTER TABLE %s ADD %s %s" % (tabletitle, self.removeSpecialCharacters(column.title), self.removeSpecialCharacters(column.datatype)))
			self.con.commit()
		except psycopg2.DatabaseError, e:
			print("Something went wrong with the database.")
			print(e) 
	def addToTable(self, value, dbtitle):
		# adds content to the table 
		# check the table for any special characters and make changes
		dbtitle = self.removeSpecialCharacters(self.cleanString(dbtitle)).lower()
		# create a data variable to store values
		data = []
		# loop through each row of values
		if isinstance(value, DatabaseData):
			data = value.data_list
		else:
			raise ValueError("Object was given the wrong data")
		self.connectToDatabase()
		# adding values to the specified table
		try:
			# get the list of data
			# variable: items = one row in the table
			# variable: data = the rows of data we are adding to the table
			for items in data:
				print items
				# clean the string in the list
				# NOTES: comma's are allowed in the table just not as a column header
				items = [self.cleanString(item) for item in items]
				# create a string of '%s' so the query can recognize the values in the list
				copy_string = re.sub(r'([a-z])(?!$)', r'\1,', '%s' * len(items))
				# add a comma and a space between the '%s' characters
				final_string = re.sub(r'(?<=[.,])(?=[^\s])', r' ', copy_string)
				# create the query string with the table title and the '%s' so the query can connect them to variables in the list
				query_string = 'INSERT INTO %s VALUES (%s);' % (dbtitle, final_string)
				# execute the string and fill in the '%s' with the values in the list
				self.cur.execute(query_string, items)
			print("Sucessfully updated table")
			# commit our changes
			self.con.commit()
		except psycopg2.DatabaseError, e:
			print("Something went wrong when trying to add data to the table")
			print(e)
	def addToTableSecond(self, value, dbtitle, tabletitle):
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
				items = [self.cleanString(item) for item in items]
				items[0] = dbtitle
				copy_string = re.sub(r'([a-z])(?!$)', r'\1,', '%s' * len(items))
				final_string = re.sub(r'(?<=[.,])(?=[^\s])', r' ', copy_string)
				query_string = 'INSERT INTO %s VALUES (%s);' % (tabletitle, final_string)
				self.cur.execute(query_string, items)
			print("Sucessfully updated table")
			self.con.commit()
		except psycopg2.DatabaseError, e:
			print("Something went wrong when trying to add data to the table")
			print(e)
	def dropTable(self, dbtitle):
		# get the table name; need to run function just in case the table was manipulated by functions of class
		dbtitle = self.removeSpecialCharacters(self.cleanString(dbtitle)).lower()
		# connect to the database
		self.connectToDatabase()
		# if the table exists drop it
		if self.checkIfTableExists(dbtitle):
			self.cur.execute("DROP TABLE %s" % (dbtitle))
			print("We sucessfully dropped %s table" % (dbtitle))
		else:
			print("There was no table with the name of %s you tried to drop" % (dbtitle))
		# commit changes
		self.con.commit()