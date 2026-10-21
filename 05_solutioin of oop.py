# Note ->
# Polymorphism means the ability of an object to take on many forms. In Python, polymorphism allows us to define methods in the child class with the same name as defined in their parent class. This allows us to use the same method name for different types of objects, and the appropriate method will be called based on the object that is calling it.



class Car:
  def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

  def get_brand(self):
        return self.__brand + "!"

  
  def full_name(self):
        return f"{self.__brand} {self.model}"

  def fuel_type(self):
        return "Petrol or deisel"

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Call the constructor of the parent class (Car)
        self.battery_size = battery_size

  def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "8kWh")
print(my_tesla.fuel_type())  # Output: Electric charge

safari = Car("Safari", "Safari")
print(safari.fuel_type())  # Output: Petrol or deisel