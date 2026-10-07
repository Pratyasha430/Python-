# Note: __init__ is a special method in Python classes, known as the constructor. It is automatically called when a new instance of the class is created. The purpose of the __init__ method is to initialize the attributes(variables) of the class with the values provided during object creation.


class Car:
  def __init__(self, brand, model):
        self.brand = brand
        self.model = model

  
my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # Output: Toyota
print(my_car.model)  # Output: Corolla

my_second_car = Car("Honda", "Civic")
print(my_second_car.brand)  # Output: Honda
# print(my_second_car.model)  # Output: Civic
