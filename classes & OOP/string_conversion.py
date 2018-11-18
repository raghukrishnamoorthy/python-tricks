class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f'A {self.color} car'
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.color}, {self.mileage})'

my_car = Car("blue", 15)
print(my_car)
print(repr(my_car))
