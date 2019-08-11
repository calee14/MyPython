# File2 - user.py

from library import Base

assert hasattr(Base, 'foo'), "you broke it, you fool!"

class Derived(Base):
	# remove the bar func and it will throw an error
	# saying that the subclass requires a bar func
    def bar(self):
        return 'bar'