'''
stores values using a hash map
hash map is a data structure that implements an associative 
array abstract data type, a structure that can map keys to 
values. a hash table uses a hash function to compute an index
into an array of buckets or slots, from which the desired 
value can be found.
'''

d = {}
l = []

d[1] = 'yes'
d['l'] = 'no'

d[2] = 9000

class my_class:
	def __init__(self):
		self.data = 'data'

instance = my_class()

d['object'] = instance

d.keys() # returns all keys

d.items() # returns tuples a key-value pair

for key, value in d.items(): # can't trust that they will be in order
	pass


class_names = ['jack', 'bob', 'mary', 'jeff', 'ann', 'pierre', 'martha', 'clause', 'pablo', 'susan', 'gustav']

def create_dataset():
	import random
	num_entires = 50000
	f = open('data.txt', 'w')
	for i in range(num_entires):
		current = random.choice(class_names)
		f.write(current+'\n')
	f.close()

def read_dataset_list():
	class_counts = []
	for c in class_names:
		class_counts.append(0)
	with open('data.txt', 'r') as f:
		for line in f:
			line = line.strip()
			if line != '':
				class_counts[class_names.index(line)] += 1
	print(class_counts)

def read_dataset_dict():
	class_counts = {}
	for c in class_names:
		class_counts[c] = 0
	with open('data.txt') as f:
		for line in f:
			line = line.strip()
			if line != '':
				class_counts[line] += 1
	print(class_counts)

import time

t0 = time.time()
create_dataset()
t1 = time.time()
print('Dataset creation took %f seconds\n' % (t0-t1))

t0 = time.time()
read_dataset_list()
t1 = time.time()
print('List took %f seconds\n' % (t0-t1))

t0 = time.time()
read_dataset_dict()
t1 = time.time()
print('Dictionary took %f seconds\n' % (t0-t1))
