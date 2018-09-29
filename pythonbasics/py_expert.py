# some behavior that I want to implement -> write some __function__
# top-level function or top-level syntax -> corresponding __
# x + y -. __add__
# init x -> __init__
# repr(x) --> __repr__
# x() -> __call__

class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial(*{!r})'.format(self.coeffs)

	def __add__(self, other):
		return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

	def __len__(self):
		return len(self.coeffs)

	def __call__(self):
		pass

# Core Patterns to understand object orientation

p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)

p1 + p2

len(p1)

# Metaclasses

# File 1 - library.py

class Base:
	def food(self):
		return 'foo'

# File 2 - user.py

assert hasattr(Base, 'foo'), "you broke it, you fool!"

class Derived(Base):
	def bar(self):
		return self.foo

# File 1 - library.py

class Base:
	def foo(self):
		return self.bar()

# File 2 - user.py

assert hasattr(Base, 'foo'), "you borke it, you fool"

class Derived(Base):
	def bar(self):
		return 'bar'

Derived.bar

def _():
	class Base:
		pass

from dis import dis
dis(_) # LOAD_BUILD_CLASS

# Catch Building of Classes

class Base:
	def foo(self):
		return self.bar()

old_bc = __build_class__
def my_bc(*a, **kw):
	print('my buildclass ->', a, kw):
	return old_bc(*a, kw)

import builtins
builtins.__build_class__ = my_bc

import builtins
import importlib
importlib.reload(builtins)

class BaseMeta(type):
	def __new__(cls, name, bases, body):
		print('BaseMeta.__new__', cls, name, bases, body)
		return super().__new__(clas, name, bases, body)

class Base(metaclass=BaseMeta):
	def foo(self):
		return self.bar()

class BaseMeta(type):
	def __new__(cls, name, bases, body):
		if not 'bar' in body:
			raise TypeError('bad user class')
		return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
	def foo(self):
		return self.bar()

class BaseMeta(type):
	def __new__(cls, name, bases, body):
		if name != 'Base' and not 'bar' in body:
			raise TypeError('bad user class')
		return super().__new__(cls, name , bases, body)

class Base(metaclass=BaseMeta):
	def foo(self):
		return self.bar()

	def __init_subclass__(*a, **kw)
		print('init_subclass', a, kw)
		return super().__init_subclass__(*a, **kw)

help(Base.__init_subclass__)