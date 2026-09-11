# Question no. 6-->
# number = int(input("Enter your number: "))
# factorial = 1

# while number>0:
#  # factorial = factorial * number
#  # number = number - 1
#  factorial *= number
#  number -= 1

# print("factorial is: ", factorial)


# Question no. 7-->

# while True:
#  number = int(input("Enter your number: "))

#  if  1 <= number <= 10:
#   print("Thanks")
#   break
#  else:
#   print("Invalid number")


# Question no. 8-->

# number = int(input("Enter your number: "))
# is_prime = True

# if number > 1:
#  for i in range(2, number):
#   if (number % i) == 0:
#    is_prime = False
#    break

# print( is_prime )


# Question no. 9-->

# items = ["apple", "Banana", "Orange", "apple", "mango"]
# unique_item = set()

# for item in items:
#  if item in unique_item:
#   print("Duplicate:", item)
#   break

# unique_item.add(item)


# Question no. 10-->

# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while attempts < max_retries:
#  print("Attempt", attempts + 1, " - Wait time", wait_time, )
#  time.sleep(wait_time)
#  wait_time *= 2
#  attempts += 1