'''
this is an io bound task
meaning there is an input and output
the code runs linearly
'''

import time

def two():
	print('starting two')
	time.sleep(2)
	print('hey two')

def four():
	print('starting four')
	time.sleep(4)
	print('hey four')

start = time.time()
two()
four()
print(f'{time.time()-start}')