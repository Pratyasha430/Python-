username = "chaiaurcode"

def func():
 username = "chai"
 print(username) # this will print the local variable username

print(username) #chaiaurcode
func() #chai # this will print the local variable username

def func():
  # username = "chai"
  print(username)


print(username) #chaiaurcode
func() #chaiaurcode # this will print the local variable username



x = 99

def func2(y):
  z = x + y
  return z

result = func2(1) # this will give an error because y is not defined in the local scope of func2() function. 
print(result) #100


x = 99

def func3():
  x = 88

print(x)  #99 # this will print the local variable x


# x = 99

# def func3():
#   global x # this will tell the function to use the global variable x instead of creating a local variable x
#   x = 88

# func3()  # 88 # this will change the value of global variable x to 88
# print(x)  #88 # this will print the updated value of global variable x


def f1():
  x = 88
  def f2():
    print(x) # this will print the local variable x of f1() function
  f2()
f1() #88 # this will print the local variable x of f1() function


def f1():
  # x = 88
  def f2():
    print(x) # this will print the global variable x
  f2()
f1() #99 # this will print the global variable x 


def f1():
  x = 88
  def f2():
    print(x) # this will print the global variable x
  return f2
  f2()
myResult = f1()
myResult() #88 # this will print the local variable x of f1() function 


def chaiCode(num):
  def actual(x):
    return x ** num
  return actual

f = chaiCode(2) # this will return the actual function with num = 2
g = chaiCode(3) # this will return the actual function with num = 3

print(f(5)) #25 # this will return 5 ** 2
print(g(5)) #125 # this will return 5 ** 3