# dec.py

import time as t

def timer(func):
    def f(x, y=10):
        before = t.time()
        rv = func(x, y)
        after = t.time()
        print('elapsed', after - before)
        return rv
    return f

@timer
def add(x, y=10):
	return x + y

@timer
def sub(x, y=10):
	return x - y

# Don't hardcode parameters in decorator functions
def timer_k(func):
    def f(*args, **kwargs):
        before = t.time()
        rv = func(*args, **kwargs)
        after = t.time()
        print('elapsed', after - before)
        return rv
    return f

@timer_k
def add_dec(x, y=10):
    return x + y

@timer_k
def sub_dec(x, y=10):
    return x - y

n = 2

def ntimes(f):
    def wrapper(*args, **kwargs):
        for _ in range(n):
            print('running {.__name__}'.format(f))
            rv = f(*args, **kwargs)
        return rv
    return wrapper
    
        
@ntimes
def add_dec(x, y=10):
    return x + y

@ntimes
def sub_dec(x, y=10):
    return x - y

def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print('running {.__name__}'.format(f))
                rv = f(*args, **kwargs)
            return rv
        return wrapper
    return inner
    
        
@ntimes(2)
def add_hdec(x, y=10):
    return x + y

@ntimes(4)
def sub_hdec(x, y=10):
    return x - y

# @timer is the equilvalent to 'add = timer(add)'

# Where the function is stored in memory
print(add)
# Name of function
print(add.__name__)
# What module function is assigned to
print(add.__module__)
# Default values
print(add.__defaults__)
# Byte code for function
print(add.__code__.co_code)
# Variable names function interacts with
print(add.__code__.co_varnames)

print('add(10)',       add(10))
print('add(20, 30)',   add(20, 30))
print('add("a", "b")', add("a", "b"))
print('sub(10)',       sub(10))
print('sub(20, 30)',   sub(20, 30))

print('add(10)', add_dec(10))
print('add(20, 30)', add_dec(20, 30))
print('add("a", "b")', add_dec("a", "b"))
print('sub(10)', sub_dec(10))
print('sub(20, 30)', sub_dec(20, 30))

print('add(10)', add_hdec(10))
print('add(20, 30)', add_hdec(20, 30))
print('add("a", "b")', add_hdec("a", "b"))
print('sub(10)', sub_hdec(10))
print('sub(20, 30)', sub_hdec(20, 30))