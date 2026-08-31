chai_types = {"Masala": "Spice", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types) #{'Masala': 'Spice', 'Ginger': 'Zesty', 'Green': 'Mild'}

print(chai_types["Masala"]) #Spice

chai_types.get("Gingery")
print(chai_types)

# chai_types.get["Gingery"] #(if we use '[]' it throw error )
# print(chai_types)

chai_types["Green"] = "Fresh"
print(chai_types) #{'Masala': 'Spice', 'Ginger': 'Zesty', 'Green': 'Fresh'}

for chai in chai_types:
 print(chai)
#Masala
# Ginger
# Green

for chai in chai_types:
 print(chai, chai_types[chai])
#Masala Spice
# Ginger Zesty
# Green Fresh

for key, value in chai_types.items():
 print(key, value)
#Masala Spice
# Ginger Zesty
# Green Fresh

if "Masala" in chai_types:
 print("I have masala chai") #I have masala chai

 print(len(chai_types)) #3

 chai_types["Earl Grey"] = "Citrus"
 print(chai_types) #{'Masala': 'Spice', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

 chai_types.pop("Ginger")
 print(chai_types) #{'Masala': 'Spice', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

 chai_types.popitem() #(to delete specific last item we use 'poopitem')
 print(chai_types) #{'Masala': 'Spice', 'Green': 'Fresh'}

 del chai_types["Green"] #(to delete specific item we use 'del')
 print(chai_types) #{'Masala': 'Spice'}

 chai_types_copy = chai_types.copy()

 tea_shop = {
  "chai" : {"Masala" : "Spice", "Ginger": "Zesty"},
  "Tea" : {"Green": "Mild", "Black": "Strong"}
 }
 print(tea_shop) #{'chai': {'Masala': 'Spice', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}

print(tea_shop["chai"]) #{'Masala': 'Spice', 'Ginger': 'Zesty'}
print(tea_shop["Tea"]) #{'Green': 'Mild', 'Black': 'Strong'}

print(tea_shop["chai"]["Ginger"]) #Zesty
print(tea_shop["Tea"]["Black"]) #Strong

squared_num = {x:x**2 for x in range(6)}
print(squared_num) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squared_num.clear()
print(squared_num) #{}

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value) #(to create new dictionary we use'fromKeys')

print(new_dict) #{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

new_dict = dict.fromkeys(keys, keys)
print(new_dict) #{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}

