chai = "Masala Chai"
first_char = chai[0]
print(first_char) #M (Output)

slice_chai = chai[0:6]
print(slice_chai) #Masala

num_list = "0123456789"
slice_num = num_list[:] #0123456789
slice_num = num_list[3:] #3456789
slice_num = num_list[:7] #0123456
slice_num = num_list[0:7:2] #0246
slice_num = num_list[0:7:3] # 036
slice_num = num_list[0:-7] #012
slice_num = num_list[-4:] #6789

# print(slice_num)

print(chai.lower()) # masala chai
print(chai.upper()) # MASALA CHAI
print(chai) #Masala Chai  (the value didn't change bcz string is immutable)

chai = "    Masala Chai   "
print(chai.strip()) #Masala Chai (its cut the unnessecary extra spaces)


chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger")) #Ginger Chai


chai = "Lemon, Ginger, Masala, Mint"
print(chai.split()) #['Lemon,', 'Ginger,', 'Masala,', 'Mint']
print(chai.split(", ")) #['Lemon', 'Ginger', 'Masala', 'Mint']

chai = "Masala Chai"
print(chai.find("Chai")) #7
print(chai.find("chai")) #-1[its mean when it did not fine any value it return -1]

chai = "Masala Chai Chai Chai"
print(chai.count("Chai")) #3

chai_type = "Masala"
quantity = 2
order = "I Ordered {} cupes of {} chai"

print(order.format(quantity, chai_type)) # Ordered 2 cupes of Masala chai

chai_variety = ["Lemon", "Ginger", "Masala"]
print(chai_variety) #['Lemon', 'Ginger', 'Masala']

print("".join(chai_variety)) #LemonGingerMasala
print(" ".join(chai_variety)) #Lemon Ginger Masala
print("-".join(chai_variety)) #Lemon-Ginger-Masala
print(", ".join(chai_variety)) #Lemon, Ginger, Masala

chai = "Masala  Chai"
print(len(chai)) #12 

for letter in chai:
 print(letter)
#M
#a
#s
#a
#l
#a
# 
# 
#C
#h
#a
#i
 

chai = "He said, \"Masala Chai is awesome\" " #['\' means the value treated  as it is it  the value does not consider strings'] [por por duto " use kra jai nnh ty amra '\' use krbo"]
print(chai) # He said, "Masala Chai is awesome" 

chai = "Masla\nChai"
print(chai) 
#Masla
#Chai

chai = r"Masala\nChai"
print(chai) #Masala\nChai ['r' treat value as a raw string]

chai = "Masala\\nChai" #[if we dont want to use r(raw value) than i have to use '\\' to print the value]
print(chai) #Masala\nChai

chai = r"c:\user\pwd"
print(chai) #c:\user\pwd

chai = "c:\\user\\pwd" #[if we dont want to use r(raw value) than i have to use '\\' to print the value]
print(chai) #c:\user\pwd


chai = "Masala Chai"
print("Masala" in chai)  #True #[i asked qus that in my keyword is masala present or not!!]
print("jiya" in chai) #False