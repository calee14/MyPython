# File2 - user.py
from library import library

# fails before it hits the run time enviroment
assert hasattr(Base, 'foo'), "you broke it, you fool!"

class Derived(Base):
    def bar(self):
        return self.foo