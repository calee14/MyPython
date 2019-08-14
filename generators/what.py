# lazy vs eagerness
#
# one gives you all of the computation
# the other one eargerly gives you the computation as you go

# pipelines

from time import sleep
from random import randrange
from itertools import islice, tee

nwise = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))
windowed_averages = lambda g, n=2: (sum(xs)/len(xs) for xs in nwise(g, n))

print(list(nwise('abcdef')))

def compute():
	sleep(.1)
	return randrange(10)


def f():
	while True:
		yield compute()

# for x in windowed_averages(f(), 3):
# 	print(x)

class F:
	@staticmethod
	def first():
		print('first')
	@staticmethod
	def second():
		print('second')
	@staticmethod
	def last():
		print('last')

f = F()
f.first()
f.last()
f.second()

def f():
	print('first')
	yield
	print('second')
	yield
	print('last')
	yield

fi = f()
next(fi)
next(fi)
next(fi)

def task(msg):
	while True:
		# yielding control back to the scheduler
		yield
		print(msg)

def scheduler(*tasks):
	# figures out how to inter link these tasks
	while True:
		for t in tasks:
			next(t)
# use generators for the async mechanism for single processes
scheduler(task('hello'), task('goodbye'))
