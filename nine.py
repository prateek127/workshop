#day nine

#lambda function
#lambda p1, p2: p1 + p2
# total =  lambda a,b: a*b
# print(total(10,5))

#map, filter - built in higher order function, direct usegarna painxa
#map(function, iterable)

a = [1,2,3,4,5]
# output = []
# for i in a:
#     output.append(i+1)
# print (output)


# def increment(n):
#     return n+1
# output = map(increment, a)
# print(output)
# print(list(output))
# print(a)


# output = map(lambda n:n+1, a)
# print(output)
# print(list(output))
# print(a)


# names = ["ram", "shyam", "sita", "hari"]
# print(list(map(lambda i:i.title(),names)))
# print(list(map(lambda i:i.capitalize(),names)))

# a = [1,2,3,4,5]
# odd = list(filter(lambda n: n%2 != 0, a))
# print(odd)

# emails = ["1@gmail.com", "2@yahoo.com", "3@outlook.com", "4@gmail.com","gmail.com07"]
# gmail = list(filter(lambda i: i.endswith("@gmail.com"), emails))
# print(gmail)

# a = [1,2,3,"ahah","apply",5,6,7]
# b = list(filter (lambda n: isinstance(n,int), a))
# print(b)
# s = 0
# a = [1,2,3,"ahah","apply",5,6,7]
# s = sum((filter (lambda n: isinstance(n,int), a)))
# print(s)


"""
object oriented python
    1. class and object
    2. inheritance -> 'is a relationship'
    3. polymorphism
        - method of overriding
    4. abstraction


"""

# class Car: #property and function
#     #initialization function ma value haru initialize garnu paryo
#     def __init__(self, model, color):
#         self.model = model #rhs ma vako model chae function ko parameter bata aako ho
#         self.color = color #lhs ma object ko attribute ko value 

# c = Car("2022","black")
# print(c.model)
# print(c.color)



# #decorator function
# def decorate_function(func):
#     def wrapper():
#         print("Hello boys !!!")
#         func()
#         print("Bye boys !!!")
#     return wrapper

# @decorate_function
# def welcome():
#     print("Welcome boys !!!")
# # a = decorate_function(welcome)
# #a()
# welcome()


# def outer(func):
#     def inner():
#         print("Hello boys!!!")
#         func()
#     return inner

# @outer
# def welcome():
#     print("Welcome Boys!!!")
# welcome()


# def zerocheck(func):
#     def wrapper(a,b):
#         if b == 0:
#             return "DIVISION BY ZERO IS NOT ALLOWED"
#         else:
#             return func(a,b)
#     return wrapper

# @zerocheck
# def division(a,b):
#     return a/b
# print(division(10,5))
# print(division(10,0))



# heroes = ["Captain America","Thor", "Hulk", "Spiderman"]
# # 1) length of the list
# print("Number of heroes = ", len(heroes))
# #add black panther the end of list
# heroes.append("Black Panther")
# print(heroes)
# #add black panther after hulk 
# heroes.pop()
# print(heroes)
# heroes.insert(3,"Black Panther")
# print(heroes)
# #remove hulk spiderman and add doctor strange in one line code
# heroes[1:3] = ["Doctor Strange"]
# print(heroes)
# #sorting list
# heroes.sort()
# print(heroes)