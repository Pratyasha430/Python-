# Note: here in the full-name functioin we use return f"{self.brand} {self.model}" because we want to return the full name of the car, which is the combination of its brand and model.


class Car:
  def __init__(self, brand, model):
        self.brand = brand
        self.model = model

  def full_name(self):
        return f"{self.brand} {self.model}"

  
my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.full_name())  # Output: Toyota Corolla

my_second_car = Car("Honda", "Civic")
print(my_second_car.brand)  # Output: Honda
print(my_second_car.full_name())  # Output: Honda Civic
# print(my_second_car.model)  # Output: Civic