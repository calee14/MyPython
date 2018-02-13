# This python program is supposed to get the data from our webscrapers and input it to the sql databases.
The python scraper class should be able to connect to the database and once connected it should be able to create tables and change it accordingly. The scraper would would have a function to connect to the database. It would have a function to create a table in the database. It would also have a function to add, update, and remove the properties of the table created. It would be best to orgainize the data in arrays when you are trying to update the table. The function will take in an array or multiple arrays and for each array it take in those elements in that array.
# How this database creator works 
	Function connect to database, parameters: database name, user, password
		run code to connect to database
	Function create a table in the connected database, parameters: database_name, and it's cell names
		create the table name
		for each cell name in the cell name list we would alter the table by add a new column and it's datatype. 
		NOTE: we could use a tuple
	Function add to the table we created, paremters: values (added values should be in arrays for it to work)
		for each array in the arrays we are adding 
			take the properties and add it to the table 
			NOTE: also use tuples for this to hold hold mulitple data, the value and the datatype.
# TODO: make it possible to add values to the database and make it work according to the data.
# New Plan 2/12/18:
The DatabaseData Class is going to organize the data that is being add to the DatabaseCreator. This class is going to include a container for table scrapers or regular scrapers (my definition for regular scrapers is just one that scrapes texts or writing). 
	class DatabaseData()
		init()
			initialize the containers stored data for either a table scraper or regular scpaper
		add row of data(value)
			Array row // for storing the data from table
			add the value to the row // operate a check on the data being passed in
			add the row to the container for table scapers
		check if data is a tuple
			run a condition to check if the data is a tuple // the tuples will help us with data types in sql commands
# Update Plan 2/12/18
Title for colums in sql database table
String -> 1. move numbers in beginning of string to end
		  2. remove spaces and any special characters
		  3. capitalize first word
INSERT INTO TableName VALUES FOR (column name*)
*(value which we get from the DatabaseData class)*