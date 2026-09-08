# this whole file will run in integrated terminal not in the regular terminal

import time
print("Chai is here")
username = "jiya"
print(username)

f = open("iteration_tools.py")
# print(f.readline())

print(f.__next__())

for line in open("iteration_tools,py"):
 print(line)

for line in open('iteration_tools.py'):
  print(line, end='') #(we use end='' to erase the extra enter/lines)


while True:
     line = f.readline()
     if not line: break
     print(line, end='') 
     # (output)
     # this whole file will run in integrated terminal not in the regular terminal

#      import time
#      print("Chai is here")
#      username = "jiya"
#      print(username)

#      f = open("iteration_tools.py")
# #    print(f.readline())

#      print(f.__next__())

#      for line in open("iteration_tools,py"):
#        print(line)

#      for line in open('iteration_tools.py'):
#        print(line, end='') #(we use end='' to erase the extra enter/lines)



test = "jiya"
if not test:  
     print("pratyasha")


test = ''             
if not test :         
     print('pratyasha') #pratyasha

myList = [1, 2, 3, 4]
I = iter(myList) 
print(I) #<list_iterator object at 0x000002C7F4A105B0>

I.__next__()# 1
I #<list_iterator object at 0x000002C7F4A105B0>
I.__next__() #2
I.__next__() #3
I.__next__() #4
I.__next__()
# Traceback (most recent call last): #StopIteration

# FOR INTERVIEW-->
# memory reference se list iteration always point at the starting point 


# FOR FILR->
f = open('iteration_tools.py')
iter(f) is f #True
iter(f) is f.__iter__() #True

# iter(f) and f is same only for file not for list


# FOR LIST->
myNewList = [1, 2, 3]         
iter(myNewList) is  myNewList  #False

# when we store a file in a memory its an iteratable object by itself but if we use list in a memory location its not an iterable object by iteslf (it is the reference if actual file)

# dictionary is also an iterable 

#FOR dictionary->
D = {'a': 1, 'b': 2}
for key in D.keys():   
    print(key) 
#a(output)
#b(output)

I = iter(D)
I #<dict_keyiterator object at 0x000002C7F69850D0>
next(I)
#'a'(output)
next(I)
#'b'(output)
next(I) #StopIteration


#NOTE->
# range is also an iterable object

#FOR range--->

range(0, 5) #range(0, 5)
R = range(0, 5)
R
# range(0, 5)
I = iter(R)
next(I) #0
next(I) #1
next(I) #2
next(I) #3
next(I) #4
next(I) #StopIteration