#python operators

"""
1. Arithmetic operator
2. Comparison
3. Equality
4. Logical
5. Bitwise
6. Shift
7. Assignment
8. Ternary
9. Membership
10. Identity
"""

"""
1. Arithmetic operator
a. Addition
b. Subtraction
c. Multiplication
d. Division
e. Modulus(%)
f. Exponential operator(**)
g. Floor division(//)
"""

a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

"""
2. Comparison operator
a. Greater than (>)
b. Greater than equal to(>=)
c. Less than(<)
d. Less than equal to(<=)
"""
a=10
b=5
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

s1="Cat" #67
s2="Dog" #68
print("------------------")
print(s1>s2)
print(s1>=s2)
print(s1<s2)
print(s1<=s2)
# to get the asci value there is a function called as ord
print(ord("C"))
print(ord("c"))

print('apple'>'apple')
print('apple'>='apple')
print('apple'<'apple')
print('apple'<='apple')

# Relational operator chaining
print(10<20<30<40)

"""
3. Equality Operators
a. Equal to(==)
b. Not Equal to(!=)
"""
print("############Equality Operators#############")
a=10
b=20
print(a==b)
print(a!=b)
print("------------------Equality Operators-----------------")
print(1==True)
print(0==False)
print(10==10.0)
print("Way2Automation" =="Way2Automation")

"""
4. Logical Operators

a. And  --> Return True when both the arguments are True in nature
b. Or   --> Return True if atleast one argument is True
c. Not  --> return the reverse
"""
print("---------Logical Operators-------------------")

print("-------AND---------")

print(True and True)
print(1 and 0)
"""
a. if the value x , evaluates to False, then the result is value x
b. if the value x, evaluates to True, then the result is the value y
"""

print(10 and 20)
# claude explain
#Python's and doesn't return True/False — it returns one of the actual values.
#It checks the first value: if it's "empty/zero/false-ish," it stops and returns that. Otherwise, it moves to the second value and returns that one, no matter what it is.
#10 and 20 → 10 isn't empty/zero, so move on → return 20.

print(0 and 20) # value is 0

print("---------OR------------")

print(10 or 20) #10

print(0 or 10) #10


# username =input("Enter your username :")
# password = input("Enter your password :")
#
# if username =="way2automation" or password =="Test":  # use of and/or operator
#     print("valid user")
# else:
#     print("invalid user")


print("---------NOT---------------")
print(not True)
print(not False)
a=10
print(not a==10)













