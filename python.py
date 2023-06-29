# str.py
#str class
str="preparing coffee"
x=str.title()
print (x)
#preparing coffee
str= "GRINDING COFFEE BEANS"
x=str.lower()
print (x)
#grinding coffee beans
str= "Boiling water"
x=str.upper()
print (x)
#BOILING WATER
str= "brew coffee"
x=str.count('coffee')
print (x)
#1
str= "serve_coffee"
x=str.isupper()
print (x)
# False
str= "here is your coffee"
x=str.islower()
print (x)
# True
str= "coffee tastes so good"
x=str.find("good")
print (x)
#17
str="forgot to add sugar"
x=str.isnumeric()
print(x)
#False
str= "stir it well"
x=str.capitalize()
print(x)
#Stir it well
str= "making coffee is easy"
x=str.isidentifier()
print(x)
#False
