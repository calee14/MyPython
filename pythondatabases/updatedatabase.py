import sys
import psycopg2

con = None
def updatedata(values):
	for value in values:
		