# gen.py - use whenever sequencing is needd

# top-level syntax, function -> underscore method
# x()               __call__

def add1(x, y):
    return x + y

class Adder:
    def __init__(self):
        self.z = 0
        
    def __call__(self, x, y):
        self.z += 1
        return x + y + self.z

add2 = Adder()

from time import sleep
# This example has storage... and has eager return of the result sets
def compute():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv
'''
Wasteful because we have to wait for the entire action to complete 
and be read into memory, when we really just care about each 
number (one by one)
'''
class Compute:
    def __call__(self):
        rv = []
        for i in range(100000):
            sleep(5)
            rv.append(i)
        return rv
    
    def __iter__(self):
        self.last = 0
        return self
    
    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return self.last

#This is too ugly to read ^^^

# This is a generator... don't eagerly compute. Return to user as they ask for it...

def compute():
    for i in range(10):

        # performs some computation

        sleep(.5) # sleep models the complex computation

        # give the value back to the user to do something
        yield i # -> used for generators/sequencing	
'''
Core concept and mental model of a generator
Instead of eagerly computing values you give 
it to the user as they ask for it

Let a little library code run, then
let a little user code run
Let a little library code run, then
let a little user code run

Interleave them
Core conceptualization of generators
'''

for val in compute():
    # user do what ever they want to do with value
    print(val)

# for x in xs:
#    pass

# xi = iter(xs)    -> __iter__
# while True:
#   x = next(xi)   -> __next__

class Api:
    def run_this_first(self):
        first()
    def run_this_second(self):
        second()
    def run_this_last(self):
        last()

# can ensure that the first func will always 
# run before the second and third
def api():
    first()
    yield
    second()
    yield
    last()
