# Question no. 6-->

def cube(num):
    return num ** 3 # cube function return the cube of a number

print(cube(5)) #125 
#Alternative process to define a function using lambda function

# Alternate method->
cube = lambda x: x ** 3 # cube store a lambda function 
print(cube(5)) #125 
# calling cube function with argument 5

# Question no. 7-->

#NOte ---> * --> with this * you can pass any number of arguments to a function.

def sum_all(*args):
    print(args) # print the tuple of arguments
    for i in args: # iterate through the tuple of arguments
        print(i * 2) # print the double of each argument
    return sum(args) # return the sum of all arguments

print(sum_all(1, 2, 3))
# (output of print(args))
# (1, 2, 3)
# 2
# 4
# 6
# 6


# Alternative method->

def sum_all(*args):
    print(*args) # print the arguments without tuple
    return sum(args) # return the sum of all arguments

print(sum_all(1, 2, 3)) #1 2 3
                        #6
print(sum_all(1, 2, 3, 4, 5)) # you can pass any number of arguments to the function  
#1 2 3 4 5
#15 


# Question no. 8-->

# NOTE ---> ** --> with this ** you can pass any number of keyword arguments to a function. for example, if you want to pass a dictionary of keyword arguments to a function, you can use **kwargs. in that case you have to use for loop to iterate through the dictionary of keyword arguments and to print the key and value we use formating(print(f"{key}: {value}")) string.

def print_kwargs(**kwargs):
    print(kwargs) # print the dictionary of keyword arguments
    for key, value in kwargs.items(): # iterate through the dictionary of keyword arguments
        print(f"{key}: {value}") # print the key and value of each keyword argument

print_kwargs(name="John", age=30, city="New York") # calling the function with keyword arguments
print_kwargs(country = "USA")
print_kwargs(language = "Python", version = 3.8, framework = "Django") # calling the function with keyword arguments
# Outut-->
#{'name': 'John', 'age': 30, 'city': 'New York'}
# name: John
# age: 30
# city: New York
# {'country': 'USA'}
# country: USA
# {'language': 'Python', 'version': 3.8, 'framework': 'Django'}
# language: Python
# version: 3.8



# Question no. 9-->

# [But i dont want list so this is not the correct method for this question]
def even_generator(limit):
    li = []
    for i in range(2, limit+1, 2): # iterate through the range of limit
        li.append(i) # append the even number to the list (its gave list of even numbers'[]')
    return li # return the list of even numbers

print(even_generator(10)) # calling the function with limit 10
      #[2, 4, 6, 8, 10](output of print(even_generator(10)) for using li.append(i) method) 
      

    
# Main method that works for this qus--->

# NOTEE---> yield  also return value but it keep the value and state(abhi app itna kaam kr chuke ho) in the memory(like its place and etc. {in the merory the value  store like this [2, 4, 6, 7] } like if we have call a number 1st time and it return 2 and then  we call 2nd time and this time  it return  4 not the same 2 {means not from the first }. so yield remember the position of the number in the memory and prevents from  mixup with  number of the other functions that store  in the same memory) and it will return the value one by one when we call the function. so this is the correct method for this question.

# if i call return instead for yield then it will return the value but it will not keep the value in the memory and it will return only one value not the one by one value . so return is not the correct method for this question.


def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

#Note--->
# here we use even_geneter functtion it give us the 'even raenge' value one by one when we call the function. so this is the correct method for this question.

for num in even_generator(10): # calling the function with limit 10
    print(num) # print the even number one by one

# Output-->
# 2  
# 4
# 6
# 8
# 10


#Question no. 10-->

def factorial(n):
    if n == 0 : # base case
        return 1
    else:
        return n * factorial(n - 1) # recursive case

print(factorial(5)) # calling the function with argument 5 
#120

# here we use n- 1 bcz we want to calculate the factorial of n-1 and multiply it with n to get the factorial of n. 