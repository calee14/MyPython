import sys
import psycopg2

class databasecreator(object):

	def __init__ (self):
		self.con = None
		self.cur = None
	def connectToDatabase(self):
		self.con = psycopg2.connect("host='localhost' dbname='careersearchdb' user='postgres' password='capsdatabase'")
		self.cur = self.con.cursor()
		print("Sucessfully connect to database.")

	def createTable(self):
		self.connectToDatabase()
		try:
			# con = psycopg2.connect("host='localhost' dbname='careersearchdb' user='postgres' password='capsdatabase'")
			# cur = con.cursor()
			# print("Sucessfully connect to database.")
			self.cur.execute(
			"CREATE TABLE MajorOccupations(id serial PRIMARY KEY, occupation_title VARCHAR(255) UNIQUE NOT NULL, occupation_code VARCHAR(255) UNIQUE NOT NULL, employment_2016 VARCHAR(255) NOT NULL, employment_2026 VARCHAR(255) NOT NULL, change_2016 VARCHAR(255) NOT NULL, change_2026 VARCHAR(255) NOT NULL, median_wage VARCHAR(255) NOT NULL)")
			print("Successfully created table")
			self.con.commit()
		except psycopg2.DatabaseError, e:
			print("Something went wrong with the databse.")
			print(e)
	def addToTable(self, values):
		
