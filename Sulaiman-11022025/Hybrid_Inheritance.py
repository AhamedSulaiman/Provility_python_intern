class Vehicle:
    def show(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_feature(self):
        print("Car has 4 wheels")

class Boat(Vehicle):
    def boat_feature(self):
        print("Boat can float on water")

class Both(Car, Boat):
    def Both_feature(self):
        print("Can travel on both land and water")

obj = Both()
obj.show()
obj.car_feature()
obj.boat_feature()
obj.Both_feature()
