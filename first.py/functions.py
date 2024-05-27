#What are functions: is the group of statement in program to perform a specific task

#user define function

#Sythex function in python

def sumf(arg1,arg2):
    print(arg1 + arg2)
    
sumf(10,30)

#parameters, Arguments, Return

def sumf(name, age):
   print(name)
   print(age)

sumf("Dakalo", 26)

#How to return a value from a function

def sumf(n1, n2):
 c = n1 + n2
 return c

num = sumf(10,20)
print(num)


#Include a function accepts to value types, strings

def sum(inp1, inp2):
    if type(inp1) == type(inp2):
        return inp1 + inp2
    else:
        return "Datatypes are different."
    x = sum("Dakalo", 11)
    print(x)

#Arguments have 4 types 1. Positional Arguments,2. Keyword Arguments, 3. Default Arguments

#POSITIONAL ARGUMENTS 

def shop(item, price):
    print("Item:", item)
    print("Price:", price)

shop(price=50, item="Sugar")

#Variable lenght arguments

def std(name, clas, **marks):
    print("Name:", name)
    print("Class:", clas)
    # print("Marks:", marks)

for x,   in marks:
    print("Marks:", x)
    
std(name="Dakalo", clas=10, english=90, maths=95, physics=94)


#LocaL and Global Variable

x = 10
y = 20

def sum(x, y)

z = 50

print(x)
print(y)
print(z)

sum(x, y)

print("----")
print(x)
print(y)
print(z)

