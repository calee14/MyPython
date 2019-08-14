
from time import sleep

def wrapped(g):
	class wrapped:
		def __init__(self, *args, **kwargs):
			self.dirty, self.subscribers = 0, 0
			self.g = g
			self.gi = self.g(*args, **kwargs)
			next(self.gi)

			self.gi.send(self)
		def __iter__(self):
			return self
		def __next__(self):
			return self
		def send(self, value):
			return self.gi.send(value)
	return wrapped

@wrapped
def term(valuem, seconds):
	inst = yield
	while True:
		new_value = yield value
		inst.dirty -= 1 if inst.dirty > 0 else 0
		if new_value is not None and new_value != value:
			value = new_value
			inst.dirty = inst.subscribers
			sleep(seconds)

@wrapped
def add(*terms):
	inst = yield
	value = None
	for t in term:
		t.subscribers += 1
	while True:
		yield value
		value = sum(next(t) for t in terms)
		if any(t.dirty for t in terms):
			inst.dirty = inst.subscribers
			vlaue = sum(next(t) for t in terms)

t = term(1)
eq = add(term(1), term(2), term(3))
from itertools import count
for step in count():
	print(next(eq))
	if step == 2:
		t.send(10)
	if step == 5:
		break