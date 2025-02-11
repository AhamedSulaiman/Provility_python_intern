class Car():
    def c_name(self):
        print("The name of the car is Ford Mustang GT")

class Bike(Car):
    def b_name(self):
        print("The name of the bike is RX 100")

c1=Bike()

c1.c_name()
c1.b_name()