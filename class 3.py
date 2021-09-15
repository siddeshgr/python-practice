# 1. Creating New List
newList = [12,34,56,]
print("New List",newList)

# 2.  Adding new items to list
# 2.1 Adding New element to list syntax-->  ListName.append(value)
newList.append("100.90")
print("After append",newList)

# 2.2 Inserting at perticular location(index)
newList.insert(3,80000009)
print("After insert:",newList)

# 3. Length of list
print("List contain elements:",len(newList))

# 4. Accessing elements from list
# 4.1 Indexing list elements
print("last element :",newList[-1])
print("First element :",newList[0])
print("First to 3rd element :",newList[0:2])

# 5. Deleting Elements from List
fruits = ["Orange","Apple","Banana","Mango","Grapes"]

print("Starting List",fruits)
# 5.1 getting and removing elements from list using pop
print("1st Poped element : ",fruits.pop())
print("After 1st pop",fruits)

print("2nd Poped element : ",fruits.pop())
print("After 2nd pop",fruits)

print("3rd Poped element : ",fruits.pop(1))
print("After 3rd pop",fruits)

fruits.append("New fruite")
print("After adding neew fruite",fruits)


# 5.2 Remove(Value)
fruits.remove("New fruite")
print("After removing 'New fruite'",fruits)

# 6. Empty the list
fruits.clear()
print("After Clearing Elements",fruits)


# 2. Tuple

# 1 Creating Tuples
Courses = ("CS","Mech","Civil","EC","E&E","EEE")
print("Starting Tuple:",Courses)

# 2. check variable type
print("Variable type:",type(Courses))

# 3. check length of tuple
print("Tuple Length:",len(Courses))

# 2. Accesing Elements
print("First Elemenent : ",Courses[0])
print("Last Elemenent : ",Courses[-1])
print("0 to 3 Elemenent : ",Courses[0:4])



# Advance list operations
# Multiple Lists
frist_rollnumer1 = ["aakash",89,90]
frist_rollnumer2 = ["aakash1",89,90]
frist_rollnumer3 = ["aakash2",89,90]
frist_rollnumer4 = ["aakash3",89,90]

firstStandardStudents = [frist_rollnumer1,frist_rollnumer2,frist_rollnumer3,frist_rollnumer4]




Courses = ["CS","Mech","Civil","EC","E&E","EEE"]

New_list = Courses
print("Courses :",Courses)
print("New_list :",New_list)

New_list.append("IS")
print("After append Courses :",Courses)
print("After New_list :",New_list)


Courses = ["CS","Mech","Civil","EC","E&E","EEE"]

# Shallow copy
New_list = Courses
print("Courses :",Courses)
print("New_list :",New_list)


New_list.append("IS")
print("After append Courses :",Courses)
print("After New_list :",New_list)


# Hollow copy
New_list2 = Courses.copy()

print("Courses :",Courses)
print("New_list2 :",New_list2)


New_list2.append("New Element")
print("After append Courses :",Courses)
print("After New_list2 :",New_list2)

values = ["Hello World",1,2,3,5.0,[["A","b","c","d"],20,30,40,50,60]]

# String
print(values[0][0:5])


# List
print(values[-1][0][0:2])