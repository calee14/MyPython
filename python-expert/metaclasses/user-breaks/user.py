# File2 - user.py

assert hasattr(Base, 'foo'), "you broke it, you fool!"

class Derived(Base):
    def bar(self):
        return 'bar'