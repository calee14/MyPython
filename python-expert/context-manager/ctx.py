# cty.py

from sqlite3 import connect
from contextlib import contextmanager

# with ctx() as x:
#   pass

# x = ctx().__enter__
# try:
#   pass
# finally:
#    x.__exit__

# context managers
# some piece of code that pairs set up and tear down actions
# so that the tear down actons always occurs when the set up ocurs
# generator
# some form of syntax
# allows us to enforce sequencing and interleaving
# decorator
# wraps the contextmanager around the generator
# wraps a function or object around another piece of code

class contextmanager:
    def __init__(self, gen):
        self.gen = gen
    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)
    def __exit__(self, *args):
        next(self.gen_inst, None)
        
@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    print('created table')
    try:
    	yield
    finally:
    	cur.execute('drop table points')
    	print('dropped table')

# in this case contextmanager is the equivalent of 
# temptable = contextmanager(temptable)

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        cur.execute('insert into points (x, y) values(2, 2)')
        for row in cur.execute("select x, y from points"):
            print(row)