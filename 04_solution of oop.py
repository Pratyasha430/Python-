# Note: to stop the access of the __init__fnction we have to add double underscore before the variable name(like __brand). This is called name mangling in Python. It makes the variable private and prevents it from being accessed directly from outside the class. we can access this veriable only ni the class not from outside the class. If we want to access this variable from outside the class we can use getter method(geeter brand syntax is self.get_brand()).


class Car:
  def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

  def get_brand(self):
        return self.__brand + "!"

  
  def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Call the constructor of the parent class (Car)
        self.battery_size = battery_size

  

my_tesla = ElectricCar("Tesla", "Model S", "8kWh")
# print(my_tesla.__brand()) # output is npot given bcz __brand is private variable and we can not access it from outside the class. we can access it only in the class. if we want to access it from outside the class we can use getter method(the geeter method syntax is self.get_brand()).
print(my_tesla.full_name())  # Output: Tesla Model S

print(my_tesla.get_brand())  # Output: Tesla!

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)  # Output: Toyota
# print(my_car.model)  # Output: Corolla
# print(my_car.full_name())  # Output: Toyota Corolla

# my_second_car = Car("Honda", "Civic")
# print(my_second_car.brand)  # Output: Honda
# print(my_second_car.full_name())  # Output: Honda Civic
# # print(my_second_car.model)  # Output: Civic