from collections import namedtuple
import json
Car = namedtuple('Car', 'color make mileage')


my_car = Car('red', 'mazda', 12)
print(my_car.color)
print(my_car.mileage)

color, make, mileage = my_car

print(color)
print(make)
print(mileage)
print(my_car)


class MyCarWithMethods(Car):

    def hexcolor(self):
        if self.color == "red":
            return "RED CAR"
        else:
            return "Normal color"

c = MyCarWithMethods("red", "mazda", 12)
print(c.hexcolor())
print(c._asdict())
print(json.dumps(c._asdict()))
print(c._replace(color='blue'))
newCar = Car._make(['red', 'mazda', 15])
print(newCar)