# Question no. 1--->
# age = int(input("Enter the age: "))

# if(age < 13):
#  print("child")
# elif(age <= 19):
#  print("Teenager")
# elif(age <= 59):
#  print("Adult")
# else:
#  print("Senior")


 # Question no. 2--->

# age = int(input("Enter your age: "))
# day = input("Enter the day: ")


# if(age >= 18):
#  price = 12
# else: 
#  price = 8

# if day =="Wed":
#  price = price - 2
#  print("Everyone gets $2 discount on Wednesday")

# print("Final price is $", price)

# ////Alternative process------>

# age = 26
# day = "Wed"

# price = 12 if age >= 18 else 8

# if day =="Wed":
#  price = price - 2
#  print("Everyone gets $2 discount on Wednesday")

# print("Final price is $", price)


 # Question no. 3--->

# grade = int(input("Enter your grade: "))

# if(grade >= 101 or grade < 0):
#  print("Wrong Grading")
#  exit()

# if(grade >= 90):
#  print("Grade: A")
# elif(grade >= 80):
#  print("Grade: B")
# elif(grade >= 70):
#  print("Grade: C")
# elif (grade >= 60):
#  print("Grade: D")

# else:
#  print("Grade: F")

 # Question no. 4--->

# fruit = input("Enter your fruit: ")
# colour = input("Enter the fruit colour: ")

# if fruit == "Banana":
#  if (colour == "Green"):
#   print("Unripe") 
#  elif  colour == "Yellow":
#   print("Ripe") 
#  elif colour == "Brown":
#   print("Overripe") 
# else:
#   print("Dont have any information about this fruit")

# Question no. 5--->

# weather = input("Enter todays weather: ")

# if weather == "Sunny":
#  print("Go for a walk")
# elif(weather == "Rainy"):
#  print("Read a book")
# elif(weather == "Snowy"):
#  print("Build  a snowman")

# Question no. 6--->

# distance = int(input("Enter your distance: "))

# if distance < 3 :
#  print("Walk")
# elif(distance <= 15):
#  print("Bike")
# else:
#  print("Car")

# Question no. 7--->

# oder_size = "Medium"
# extra_shot = True

# if extra_shot:
#  coffee = oder_size + " Coffee with an extra shot"
# else:
#  coffee = oder_size + "coffee"

# print("Order:", coffee)


# Question no. 8--->

# password = int(input ("Enter your password : "))
# cha_size = len(password)

# if len(password) < 6:
#  strength = "Weak"
# elif len(password) <= 10:
#  strength = "Medium"
# else:
#  strength = "Strong"

# print ("Password Strength is: ", strength)


# Question no. 10--->

# pet = input("Enter your pet: ")
# age = int(input("Enter your pets age: "))

# if pet == "Dog":
#  if age < 2:
#   print("Puppy food")
# elif pet == "Cat":
#  if age > 5:
#   print("Senior cat food")

# else:
#  print("No food preferance for this pet")


# Question no. 10--->

year = int(input("Enter your year: "))

if (year%4 == 0 and year%100 != 0) :
 print("Leap Year")
elif(year%400 == 0):
 print("Leap Year")
else:
 print("Not a leap year")