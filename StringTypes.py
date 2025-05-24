
'''String'''
print(type("this is a string"))

# we can write string either in double quotes or single quotes

a ="Welcome to sai Dreams Phase 2"
print(a)

b ='Welcome to SAI DREAMS PHASE 2'
print(b)

''' If we want to print below statement in string then we need to print in this manner
Hey, My name is "Rahul" '''

print('Hey, My name is "Rahul"')

e = ("hey"
     "My name is"
     "Aditya")

print(e)

g ="""

hey 
My name is:
Aditya


"""

print(g)

#suppose we want top print below statement
# This is Rahul's "New" house under double quotes then we will use \ backslash

print("This is Rahul's \"New\" house")

name ="Rahul"

print(name[4])

# slicing off strings

print(name[1:4]) # will print ahu

# suppose we want to jump 1 step or 2 step then we need to do the below

print(name[1:4:2])  # wqill print au

# the below statemnent will print the whole string contained in variable name
print(name[::]) # Rahul

# the below statement will print the statement by jumping 2 charcters
print(name [::2]) # will print Rhl

# if we need to reverse the string in python we need to do below
print(name[::-1])

# if we need length of a string
print(len(name))

# if we need to remove white spaces then we need to use strip() method

abc =" Hello, Rahul "

print(abc.strip())

# to convert to lower case and upper case use below

print(name.lower())

print(name.upper())

# split a string

abc ="hello, Aditya"

b = abc.split(",")

print(b[0])
print(b[1].strip())


# concatenation  for it both the type should be same

ab ="Hi"
cd ="Way2Automation"

print(ab+cd)

#print(10+"10") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print ("10"+"10")



# Repition of strings

a ="10"*4
print(a)

print("ba"+"na"*2) # prints banana  uses BODMAS so first will be multiplication and then addition


# form of concatenation
city ="New Delhi"

print("Hey, I live in ",city)


#  use of string formatter  also called as f-Strings
# format()
# % percentage formatter

Age = 35
id =10.12

print(f"hey, I live in {city}, My Age is {Age} and id is {id}")

print("Hey, I live in {}, My Age is {}".format(city,Age,id))

print("Hey, I live in %s, My age is %d and id is %f"%(city,Age,id))





























