import sys
import psycopg2
from difflib import SequenceMatcher 
import re

# setting up connection 
con = psycopg2.connect("host='localhost' dbname='careersearchdb' user='postgres' password='capsdatabase'")
cur = con.cursor()

def letters(input):
	removelist = "=.,"
	result = re.sub(r'[\d+\s|\s\d+\s|\s\d+$'+removelist+']',' ',input)
	return result.strip()
# class to hold string and pairs
def substringFinder(string1, string2):
	streak = 0
	for i in range(len(string1)):
		if i < len(string2):
			if string1[i] == string2[i]:
				streak += 1 
			else:
				return streak
		else:
			return streak
	return -1
class Nodes():
	def __init__(self, string):
		self.title = string
		self.pairs = []
		self.streak = 0
	def __addPair(self, string, ratio):
		tup = (string, ratio)
		self.pairs.append(tup)
	def find_str(s, char):
		index = 0
		if char in s:
			c = char[0]
			for ch in s:
				if ch == c:
					if s[index:index+len(char)] == char:
						return index
				index += 1
		return -1
	def matchString(self, string):
		ratio = SequenceMatcher(None, self.title[:-12], string).ratio()
		if ratio > 0.5:
			self.__addPair(string, ratio)
		else:
			match = substringFinder(letters(self.title.lower()), letters(string.lower()))
			if match > 3:
				self.__addPair(string, float(match)/float(len(string)))
	def returnBestMatch(self):
		word = ("",0)
		for pair in self.pairs:
			if(pair[1] > word[1]):
				word = pair
		return word
# declaring the strings and organizing into lists
strings = ['Management occupations', 'Business and financial operations occupations', 'Computer and mathematical occupations', 'Architecture and engineering occupations', 'Life, physical, and social science occupations', 'Community and social service occupations', 'Legal occupations', 'Education, training, and library occupations', 'Arts, design, entertainment, sports, and media occupations','Healthcare practitioners and technical occupations', 'Healthcare support occupations', 'Protective service occupations', 'Food preparation and serving related occupations', 'Building and grounds cleaning and maintenance occupations', 'Personal care and service occupations','Sales and related occupations', 'Office and administrative support occupations', 'Farming, fishing, and forestry occupations', 'Construction and extraction occupations', 'Installation, maintenance, and repair occupations', 'Production occupations', 'Transportation and material moving occupations']
nodes = []
for string in strings:
	nodes.append(Nodes(string))
# run the tests
test_strings = ['Architecture and Engineering',
'Arts, Design, Entertainment, Sports, and Media',
'Building and Grounds Cleaning',
'Business and Financial',
'Community and Social Service',
'Computer and Information Technology',
'Construction and Extraction',
'Education, Training, and Library',
'Entertainment and Sports',
'Farming, Fishing, and Forestry',
'Food Preparation and Serving',
'Healthcare',
'Installation, Maintenance, and Repair',
'Legal',
'Life, Physical, and Social Science',
'Management',
'Math',
'Media and Communication',
'Military',
'Office and Administrative Support',
'Personal Care and Service',
'Production',
'Protective Service',
'Sales',
'Transportation and Material Moving'];

# cur.execute('ALTER TABLE major ADD occupation_group VARCHAR(500);')
for node in nodes:
	for test_string in test_strings:
		node.matchString(test_string)
	print str(node.returnBestMatch()) + " " + node.title + " streak: "
	cur.execute("UPDATE occupationdesc SET occupation_group = %s WHERE job_title = %s;", (' '.join(letters(node.returnBestMatch()[0]).split()).replace(' ', '_'), node.title))
	con.commit()

