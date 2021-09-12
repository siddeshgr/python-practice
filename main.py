#1
print("hello world")
name = input("enter your name:      ")
print("hello siddesh")

#1 variables in python
x = 100
y = 100
z = 200
print(x,y,z)

#2 float [float]
x1 = 20.20
y1 = 30.30
print(x1,y1)

name = "hello"
print("single character",name[1])

name = "hello"
print("snigle character",name[3])


# Conditions for variable name

# 1. Variable should not starts with number
# 2. Should not contain space
# 3. Should not contain special characters

# Rules for long variable name PEP8

# 1.  Single word
# a. Name -- correct
# b. name -- correct
# c. namE -- wrong

# 2.  More than one word
# a. FullName -- correct --  Title Case
# b. Full_Name -- correct
# c. full_name -- correct


#3 string indexing

name ="hello world"

length =len(name)
print("length of string;",length)
print("single character;",name[3])
print("multiple chatrater",name[0:3])
print("mulitiple character;",name[0:4])
print("multiple charater;",name[2:5])
print("multiple charatrer start to end;",name[2::])
print("last element:",name[-1])
print("multiple last elements:",name[:-3])

#4 boolean
#value = true
#negative = false
# basic maths operators ( + , - , * ,/ , % , //)
# basic maths

print("x= ",x)
print("y= ",y)

#A addition
x = 40
y = 25
z = x+y
print("addition ",z)

#B substraction
sub = x-y
print("substraction",sub)

#C multiplication
mul = x*y
print("multiplication",mul)

#D dividion
div = x/y
print("dividion",div)

#E modulus
x1= 5
y1 = 2
mod = x1%y1
print("modulus",mod)

#F division
div = x//y
print("division",div)
