# Question no. 1-->

def square(number):
 print(number **2)

square(5) #25

# ALTERNATIVE PROCESS->

def square(number):
 print(number **2)

reuslt = square(5) 
print(reuslt) #None

# if we use return-->

def square(number):
 return number **2

result = square(5)
# print(result) #25
print(square(5)) #25

# Question no. 2-->

def add(num1, num2):
 return num1 + num2

print(add(6, 9)) #15

# Question no. 3-->

def multiply(num1, num2):
 return num1 * num2

print(multiply(5, 6)) #30
print(multiply('a', 5)) #aaaaa
print(multiply(5, 'a')) #aaaaa

# Question no. 4-->

import math

def area_of_circle(radius):
 area = math.pi * radius ** 2
 circumference = 2 * math.pi * radius
 return area, circumference

a, c = area_of_circle(5)
print("Area: ", a, "Circumference: ", c) # Area:  78.53981633974483 Circumference:  31.41592653589793


# Question no. 5-->

def greet(name = "User"):
 return "Hello, " + name + "!"

print(greet("Pratyasha")) #Hello, Pratyasha!
print(greet()) #Hello, User!