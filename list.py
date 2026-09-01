tea_varities = ["Black", "Green", "Oolong", "White" ]

print(tea_varities) #['Black', 'Green', 'Oolong', 'White']
print(tea_varities[1]) #Green
print(tea_varities[-1]) #White
print(tea_varities[1:3]) #['Green', 'Oolong']
print(tea_varities[:2]) #['Black', 'Green']

# tea_varities[3] = "Herbal"
# print(tea_varities) #['Black', 'Green', 'Oolong', 'Herbal']

# tea_varities[1:2] = "Lemon"
# print(tea_varities) #['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']

print(tea_varities) #['Black', 'Green', 'Oolong', 'White']

tea_varities[1:2] = ["Lemon"]
print(tea_varities) #['Black', 'Lemon', 'Oolong', 'White']

print(tea_varities[1:3]) #tea_varities[1:2]

tea_varities[1:3] = ["green", "Masala"]
print(tea_varities) #['Black', 'green', 'Masala', 'White']

print(tea_varities[1:1]) #[]
print(tea_varities[0:0]) #[]

tea_varities[1:1] = ["test", "test"]
print(tea_varities) #['Black', 'test', 'test', 'green', 'Masala', 'White']

print(tea_varities[1:2]) #['test']
print(tea_varities[1:3]) #['test', 'test']

tea_varities[1:3] = []
print(tea_varities) #['Black', 'green', 'Masala', 'White']


for tea in tea_varities:
 print(tea)
# (output)
 #Black
 #green
 #Masala
 #White

for tea in tea_varities:
 print(tea, end="-") #Black-green-Masala-White-

if "Oolong" in tea_varities:
  print("I have Oolong tea")


tea_varities.append("Oolong")
print(tea_varities) #['Black', 'green', 'Masala', 'White', 'Oolong']

if "Oolong" in tea_varities:
  print("I have Oolong tea") #I have Oolong tea


tea_varities.pop()
print(tea_varities) #['Black', 'green', 'Masala', 'White'] (to remove last item)

tea_varities.remove("green")
print(tea_varities) #['Black', 'Masala', 'White'] (to remove item from anywhere)


tea_varities.insert(1, "green") 
print(tea_varities) #['Black', 'green', 'Masala', 'White']

tea_varities_copy = tea_varities.copy()
tea_varities_copy.append("Lemon")

print(tea_varities) #['Black', 'green', 'Masala', 'White']
print(tea_varities_copy) # ['Black', 'green', 'Masala', 'White', 'Lemon']

print(range(10)) #range(0, 10)

y = range(10)
print(y) #range(0, 10)

squared_nums = [x**2 for x in range(10)]
print(squared_nums) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube_num = [y**3 for y in range(5)]
print(cube_num) #[0, 1, 8, 27, 64]