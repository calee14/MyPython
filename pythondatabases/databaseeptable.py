import sys
import psycopg2
from databasedata import databaseData

class databasecreator(object):
	def __init__ (self):
		self.con = None
		self.cur = None
	def connectToDatabase(self):
		self.con = psycopg2.connect("host='localhost' dbname='careersearchdb' user='postgres' password='capsdatabase'")
		self.cur = self.con.cursor()
		print("Sucessfully connect to database.")

	def createTable(self, value):
		columns = None
		if isinstance(value, databaseData):
			columns = value.column_list
		else:
			raise ValueError("Object was given the wrong data")
		self.connectToDatabase()
		try:
			# con = psycopg2.connect("host='localhost' dbname='careersearchdb' user='postgres' password='capsdatabase'")
			# cur = con.cursor()
			# print("Sucessfully connect to database.")
			self.cur.execute("CREATE TABLE MajorOccupations();")
			for column in columns:
				self.cur.execute("ALTER TABLE MajorOccupations ADD %s %s;"  % (column.title, column.datatype))
				print("Altering table " + "ALTER TABLE MajorOccupations ADD %s %s;" % (column.title, column.datatype))
			print("Successfully created table")
			self.con.commit()
		except psycopg2.DatabaseError, e:
			print("Something went wrong with the database.")
			print(e)
	def addToTable(self, value):
		data = []
		# loop through each row of values
		if isinstance(value, databaseData):
			data = value.data_list
		else:
			raise ValueError("Object was given the wrong data")
		self.connectToDatabase()
		try:
			for row in data:
				self.cur.executemany("INSERT INTO MajorOccupations VALUES %s;", ((val.data,) for val in row))
			print("Sucessfully updated table")
			self.con.commit()
		except psycopg2.DatabaseError, e:
			print("Something went wrong when trying to add data to the table")
			print(e)