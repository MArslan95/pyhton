
# str=31
# print(type(str))
'''
name1="Harry"
name2="Arslan"

temp=f"this is a {name2} and he is a good boy {name1}"
print(type(temp))
print(temp)
'''

# lst=[61,2,4,5,9,44,21]
# var=type(lst)
# To find the length of the list
# var=len(lst)
# lst[2]=50
# var=lst[2]

# lst.append(100)
# To insert the data in list we use  insert function and in the function
# We prove the index and also  the value that you want to insert
# lst.insert(1,100)

# To remover the specific number from list we use remove
# lst.remove(61)

# To remove the last number from list we use pop function
# lst.pop()
# TO delelte the specific number from list we use del and provide the list index

# del lst[4]
# Delete the whole list
# del lst[]
# THis dunction also clear the list
# lst.clear()
# var=lst

# var=lst[0:5]
# Slicing  of list or array
# var=lst[0:5]

# TUPLES
# All the condition that are use in list also valid for Tuple
a = ("Arslan", "Adnan", "Hassaan")
# We can convert the tuple in to list to modify the tuple values
# a=list(a)
# a[0]="butt"
var = a
# var=type(a)
# We can not chang the value of tuple that are given at the start
# a[2]="Buttt"
# print(var)

# SETS HERE

s1 = {23, 2, 2, 2, 11, 1, 1, 7, 12, 6, 6, 3}
# If we want to add one number we use add() function
# s1.add(455454)
# If we want to add multiple number in a set so we use update function
# s1.update([12,121,423,4231,1212,2254])
# print(len(s1))
# To remve the number from the set
# s1.remove(12)
''' If we want if the number is in the set we use discard it
 help to delete the number if available else run the code
 intersection and union is also done in Set
 '''
# s1.discard(12222)
# print(s1)

# Dicitiory

arslanDict = {
    "Name": "Arslan",
    "class": "Software",
    "Mark": 87.22,
    "Duration": "4 years"
}
# TO change or update the Dicitiory
# arslanDict["Name"] ="Muhammad Hassaan"
# print(arslanDict["Name"])
# to remove the specific element we use pop
# arslanDict.pop("Duration")
# del arslanDict["Duration"]
# print(arslanDict)

'''
if elif and else condition here
print(type(age))
print(age)
age = input("Enter age\n")
age = int(age)
if(age > 18):
     print("You can drive the car")
elif(age == 18):
    print("You are a good team player")
else:
     print("You are not allow to drive your under age")
'''
'''Loop Start from here'''
# for i in range(0,100):
#     print(i)

'''Loope use  in list like this'''
# li = [1, 222, 232, "Arslan"]
# for item in li:
#     print(item)
'''Loope use  in tuples like this'''
# a = (1, 222, 232, "Arslan")
# for item in a:
#     print(item)

'''Loope use  in sets like this'''
# a = {1, 222, 232,232,222,1, "Arslan"}
# for item in a:
#     print(item)

'''Loope use  in dicitionary like this'''
# dic={
#     "Name": "Arslan",
#     "age":"26",
#     "profession":"Software Engineer"
# }
# for item in dic['Name']:
#     print(item)

'''While Loop in Python'''
# i = 0
# while(i < 100):
#     i = i+1
#     if i == 78:
#         # break
#         continue
#     print(i+1)

'''Function'''

# def greet():
#     print('Hello')
#     print('Hi')
#     print('HY')


# greet()

'''sum fucntion'''
# def sum(a, b):
#     c = a+b
#     return c
# d=sum(33, 36)
# print(d)

'''Class in Python'''


class Employee:
   def __init__(self, gname, gsalary):
        self.name = gname
        self.salary = gsalary
ars=Employee(' Arslan','15000')
print(ars.name)
print(ars.salary)
