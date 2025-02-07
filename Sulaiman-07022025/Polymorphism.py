class Mobile():
    def __init__(self,color,ram,price):
        self.color=color
        self.ram=ram
        self.price=price

    def specs(self):
        print(f"The price of {self.color} color {self.ram} RAM mobile is {self.price} rupees ")


class Car():
    def __init__(self,color,mileage,price):
        self.color=color
        self.mileage=mileage
        self.price=price

    def specs(self):
        print(f"The car which gives {self.mileage} km/L mileage is {self.color} color and the"
              f" price of the car is {self.price} rupees ")

m1=Mobile("Blue","16GB","50K")
c1=Car("Red","60","10L")

m1.specs()
c1.specs()
