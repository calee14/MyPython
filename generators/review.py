'''
three different functions which all accomplish the same thing
'''
# global z
z = 0
def add1a(x, y):
	'add x to y'
	global z
	z += 1
	return x + y + z

def add1b(x, y):
	'add x to y'
	add1b.z = 0
	add1b.z += 1
	return x + y + add1b.z

def add1c(z=0):
	def add1c(x, y):
		'add x to y'
		nonlocal z
		z += 1
		return x + y + z
	return add1c

add1d = add1c()
print(add1a(1, 2))
print(add1b(1, 2))
print(add1d(1, 2))

'''
lambda can only have expressions
can't have statements
'''
add2 = lambda x, y: x + y
add2.__doc__ = 'add x to y'
add2.__name__ = 'add2'

print(f'add1: {add1a(1, 2)}')
print(f'add2: {add2(1, 2)}')
help(add1a)
help(add2)

class Adder:
	def __init__(self):
		pass
	def __call__(self, x, y):
		return x + y

add3a = Adder()
add3b = Adder()
print(f'add3a: {add3a(1, 2)}')
print(f'add3b: {add3b(1, 2)}')

from time import sleep
from random import randrange

def compute():
	sleep(.1)
	return randrange(10)

print(compute())

def f():
	rv = []
	for _ in range(10):
		rv.append(compute())
	return rv

# print(f'f: {f()}')
print(f'f: {[x for x in f()]}')

print('-' * 80)

'''
this version doesn't use much storage
gave us the results when we wanted
very efficient in a memory and time perspective
'''
class F:
	def __iter__(self):
		self.size = 10
		return self
	def __next__(self):
		if not self.size:
			raise StopIteration
		self.size -= 1
		return compute()
	# def __call__(self):
	# 	rv = []
	# 	for _ in range(10):
	# 		rv.append(compute())
	# 	return rv

f = F()
# print(f'f: {f()}')

print(f'f: {[x for x in f]}')

print('-' * 80)

def f():
	for _ in range(10):
		yield compute()

print(f'f: {[x for x in f()]}')

# python turns this when using a for loop
#
# for x in xs:
#	print(x)
# 
# xi = iter(xs)
# while True:
#	try:
# 		x = next(xi) - next interator
#	except StopItertion:
# 		break
