#changing case of a string
#upper()
name="my name is Jayashree"
print(name.upper())
#lower()
name="My Name is Jayashree"
print(name.lower())
#swapcase()
name="my name is Jayashree"
print(name.swapcase())
#tittle()
name="my name is Jayashree"
print(name.title())
#Captilise()
name="my name is Jayashree"
print(name.capitalize())

#isalnum()
name="my name is Jayashree01"
print(name.isalnum())
name="mynameisJayashree01"
print(name.isalnum())
name="my name is Jayashree 1998"
print(name.isalnum())

#isalpha()
name="my name is Jayashree 1998"
print(name.isalpha()) #False
name="My name Is Jayashree"
print(name.isalpha())#False
name="MY NAME IS JAYSHREE"
print(name.isalpha())#False
name="MYNAMEISJAYSHREE"
print(name.isalpha()) #True
name="MYNAMEISJAYSHREE 1998"
print(name.isalpha())#False

#isdigit()
myNum="Jayashree 12345"
print(myNum.isdigit()) #False
myNum="Jayashree12345"
print(myNum.isdigit())#False
myNum="JAYASHREE12345"
print(myNum.isdigit())#False
myNum="12345"         #True
print(myNum.isdigit())
myNum="  12345"       #False
print(myNum.isdigit()) 

#islower()
name="my name is Jayashree 1998"
print(name.islower())#False
name="my name is jayashree 1998"
print(name.islower()) #True
name="my name is jayashree "
print(name.islower()) #True
name="MY NAME IS JAYASHREE " 
print(name.islower())#False 

#isupper()
name="My name is Jayashree 1998"
print(name.isupper()) #False
name="My Name Is Jayashree 1998"
print(name.isupper()) #False
name="MY NAME IS JAYASHREE 1998" 
print(name.isupper()) # True
name="MYNAMEISJAYASHREE"
print(name.isupper()) #True 

#istittlecase()
name="My name is Jayashree 1998"
print(name.istitle())#False
name="My Name Is Jayashree 1998"
print(name.istitle()) #True
name="MY NAME IS JAYASHREE 1998"
print(name.istitle()) #False 

## isspace()
name="My name is Jayashree 1998"
print(name.isspace()) #False
name="MYNAMEISJAYASHREE1998"
print(name.isspace()) #False
name="  My name is Jayashree 1998"
print(name.isspace()) #False
name="  My name is Jayashree 1998   "
print(name.isspace()) #False
name="  MynameisJayashree1998   "
print(name.isspace()) #False
name="  M y n a m e i s J a y a s h r e e    "
print(name.isspace()) #False
name="  My name is Jayashree 1998   "
print(name.isspace()) #False
name="    "
print(name.isspace()) #True











