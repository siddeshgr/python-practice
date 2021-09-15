# Dictionary (key Value) pair

dct = {}
dct['Person1'] = 1
dct['Person2'] = 2
dct['Person3'] = 3

print("before",dct)

# Key can be string, int , float
dct[9] = 1
dct[9.90] = 90

# All key values must be unique
dct['Person3'] = 30
print("After",dct)


# Value Types :  Anything

dct["int"] = 1110
dct["Float"] = 1110.0001
dct["String"] = "hello World"
dct["List"] = [1,2,3,4,5,6]
dct["Tuple"] = (2,3,4,5,6,7)
dct["Dictionary"] = {"Person1" : [36,56,78,46,76,89],"Person12" : [36,56,78,46,76,89],"Person13" : [36,56,78,46,76,89]}

print(dct)


# Dictionary Functions
Marks = {"Person1" : [36,56,78,46,76,89],"Person12" : [36,56,78,46,76,89],"Person13" : [36,56,78,46,76,89]}


# Get All Keys
AllKeys = Marks.keys()

# Get All values
AllValues = Marks.values()

# Sets
# Keys
# 1. All values must be unique

A = {'A','B','C','D'}
B = {'A','B','C','D','E'}

#Union
AunionB = A.union(B)
print("AunionB :",AunionB)

# Intersection
AunionB = A.intersection(B)
print("AunionB :",AunionB)


#  Variabe / Data Types

# 1. int
# 2. Float
# 3. string
# 4. List
# 5. Tuple
# 6. Dictionary
# 7. Sets

# Condional Programming

marks  = int(input("Enter the marks:"))

print(marks)

# If condition

# if (condition)
if (marks <=34):
    print("Sorry you have failed!!1")

elif (marks >=35 and marks< 50):
    print("YOu Have Passed with Third Class rank")

elif (marks >=50 and marks< 61):
    print("YOu Have Passed with Second Class rank")

elif (marks >=60 and marks< 85):
    print("YOu Have Passed with First Class rank")

elif (marks >=85 and marks< 100):
    print("YOu Have Passed with Distinction Class rank")

else:
    print("Sorry Enter Valid Data")

print("End")


# Task
# Creat A Data of Fruits and there rate --> Dict
# User Enter Fruits
# ---  Is fruit available ?
# Print Rate of Fruit

#rate  = dct['Fruite_Name']



