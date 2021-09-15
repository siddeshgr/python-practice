# Assignment Operators
x = 100
print("Before:",x)

# x = x+10
x += 10
print("After + 10:",x)

# x = x-30
x -= 30
print("After - 30:",x)

# x = x*30
x *= 30
print("After * 30:",x)

# x = x/30
x /= 30
print("After / 30:",x)

# Comparision Operators

x = 10
y = 20

# 1. Is Equal ==
print("Is Equal",x==y)

# 2. Is greater than left > right --> is left element is greater than right element
print("Is Greater",x>y)

# 3. Is greater than left < right --> is left element is smaller than right element
print("Is Smaller",x<y)

# 4. Is greater than left >= right --> is left element is greater than or equal to right element
print("Is greater then or equal ",x>=y)

# 4. Is greater than left <= right --> is left element is smaller than or equal to right element
print("Is smaller then or equal",x<=y)

# Logical operators
# 1. and
# 2. or
# 3. &
# 4. |
marks =  67

# and --> left and right elemts must be true
print(" First Class ",marks > 60 and marks < 85)

# or --> left or right elemnt must be true for true output
print(" First Class ",True or False)

# or --> left or right elemnt must be true for true output
print(" First Class ",not(True))

# & --> logical and
print(" First Class ",marks > 60 & marks < 85)

# | --> logical and
print(" First Class ",marks > 60 | marks < 85)

# ~ --> logical not
print(" First Class ",~ (marks > 60))

# Type Casting

# Variables Types
# 1. integer
# 2. float
# 3. string


# 1. int
x = 100

# int to float --> add .0
fl = float(x)
print("int to float:",fl)

#  int To string  --> Add double quote
fl = str(x)
print("int to string:",fl)


# 2. Float Type
y = 100.04

# float --> int --> Remove numbers after .
newy = int(y)
print("float to int:",newy,y)

# float --> string --> Add double quote
newy = str(newy)
print("float to int:",newy,y)

# 3. String Type --> Remove double quote

name = "1000.09876"

# str to int
newname = float(name)
print("string to int:",newname,name)


# Variable  Type
# Int
# float
# string

# List
# Creating list [Int,float, str, int , float ]
marks = [80,70,80,45,67,89,7978.90,"Name iS"]

# Indexing List Items
print(marks[2:5])


# Creating New List
newList = []
print("New List",newList)

# Adding New element to list syntax-->  ListName.append(value)
newList.append("100.90")
print("After append",newList)

# Inserting at perticular location(index)
newList.insert(3,80000009)
print("After insert:",newList)

# Length of list
print("List contain elements:",len(newList))










