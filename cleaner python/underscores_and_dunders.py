# Single _variable means it is private
class Testy:

    def __init__(self):
        self.foo = 11
        self._bar = 12


# Single variable_ can be used if name is a reserved keyword
def make_object(item, class_):
    pass

# Double __variable causes name mangling
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42

t = Test()

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'

class Mangler():
    def __init__(self):
        self.__mia = 5

    def get_mia(self):
        return self.__mia

# __var__ is magic python methods and variables. dont use them.

# single _ is throwaway/placeholder variable
car = ('suzuki', 'red', 1995, 12)
make, _, _, mileage = car