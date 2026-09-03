tea_types = ("Black", "Green", "Oolong")
print(tea_types) #('Black', 'Green', 'Oolong')

print(tea_types[0]) #Black
print(tea_types[-1]) #Oolong
print(tea_types[1:]) # ('Green', 'Oolong')
print(tea_types[:1]) #('Black',)

# tea_types[0] = "Lemon"
# print(tea_tuples) #('tuple' objectt does nt support item assignment) //(we can change referance item but not the original one)

print(len(tea_types)) #3

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)  #('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')

print(all_tea[2]) #Black

if "Green"in all_tea:
 print("I have green tea") #I have green tea

 more_tea = ("Herbal", "Earl Grey", "Herbal")
 print(more_tea) #('Herbal', 'Earl Grey', 'Herbal') (we can change reference item)

 print(more_tea.count("Herbal")) #2

print(more_tea.count("Herv")) #0

(black, green, Oolong) = tea_types #(these '(black, green, Oolong)' treated as a variable here and the value of 'tea_types' trated as a key)
print(black) #Black
print(Oolong) #Oolong

print(type(tea_types)) #<class 'tuple'>

#//---nested tuples-------->

("", (1, 2, 3), "")