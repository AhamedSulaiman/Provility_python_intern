class Model:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

class Car(Model):
  def __init__(self, brand, model, year, color, price):
    super().__init__(brand, model, year)  # Call the parent constructor
    self.color = color
    self.price = price

  def printname(self):
    print(f"The car {self.brand} {self.model} is released in the year {self.year}.")
    print(f"The color of the car is {self.color} and its price is {self.price}.")

car_detail2 = Car("Ford", "Mustang GT", 1980, "Red", 50000)
car_detail2.printname()