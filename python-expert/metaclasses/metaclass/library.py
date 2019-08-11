class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if name != 'Base' and not 'bar' in body:
            raise TypeError('bad user class')
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def bar(self):
        return 'bar'

    def foo(self):
        return self.bar()