import sqlite3

conn = sqlite3.connect('python.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)')
	name = input("What is your name?")
def data_entry():
	number = "1234"
	c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (number, name))
	conn.commit()

create_table()
data_entry()

c.close()
conn.close()