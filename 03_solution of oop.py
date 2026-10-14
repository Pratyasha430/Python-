# Note: The ElectricCar class inherits from the Car class, so it has access to the brand and model attributes, as well as the full_name method. The ElectricCar class also has its own battery_size attribute.

# * here we use def __init__(self):because we want to initialize the attributes(variables) of the ElectricCar class when a new instance is created. the super().__init__(brand, model) [here super() means when a child class wants to use something from its parent class.] line calls the constructor of the parent class (Car) to initialize the brand and model attributes. This allows us to reuse the code in the Car class and avoid duplicating it in the ElectricCar class.
 
class Car:
  def __init__(self, brand, model):
        self.brand = brand
        self.model = model

  def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Call the constructor of the parent class (Car)
        self.battery_size = battery_size

  

my_tesla = ElectricCar("Tesla", "Model S", "8kWh")
print(my_tesla.brand)  # Output: Tesla
print(my_tesla.full_name())  # Output: Tesla Model S

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)  # Output: Toyota
# print(my_car.model)  # Output: Corolla
# print(my_car.full_name())  # Output: Toyota Corolla

# my_second_car = Car("Honda", "Civic")
# print(my_second_car.brand)  # Output: Honda
# print(my_second_car.full_name())  # Output: Honda Civic
# # print(my_second_car.model)  # Output: Civic