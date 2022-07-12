# def product(num1,num2):
#     print(num1 * num2)
# ans = product(10,10)
# print (f"Answer = {ans}")



# def product(num1,num2):
#     return(num1 * num2)
# ans = product(10,10)
# print (f"Answer = {ans}")


# def example(*args):
#     print(args) 
# example(5,6)


# def exa2(**kwargs):
#     print(kwargs)
# exa2(name = "Champu", Address = "powdergalli")

# """jaile pni keywords argument paxadi rakhne ani agadi chae positional arguments rakhne"""
# def exa3(*args, **kwargs):
#     print(args)
#     print(kwargs)
# exa3(1,2,3,4,5,6,7,name = "Champu", Address = "powdergalli")


# def profile(name,contact,address):
#     print(f"Name: {name}")
#     print(f"Contact: {contact}")
#     print(f"Address: {address}")
    
# pro = {"name": "Jethiyaa", "contact": "98766","address": "gokuldham"}
# profile(**pro)

"""ADVANCE FUNCTION"""
# def welcome(name):
#     print(f"Welcome {name}")
# def greet_ram(func):
#     func("ram")
# greet_ram(welcome)

# def square_root_ofsum(func, num1, num2):
#     return func(num1,num2)**0.5
# def add(num1,num2):
#     return num1 + num2
# print(square_root_ofsum(add,10,15))

# def outer_func():
#     def firstchild():
#         print("I am first child")
#     def secondchild():
#         print("I am second child")
#     firstchild()
#     secondchild()
# outer_func()
# # firstchild()
# # secondchild() yesto garna paudaina kina ki yo duitai fn chae local scope ma xa global scope ma xaina


# def calculator(operator):
    # def add(a,b):
    #     return a+b
    # def product(a,b):
    #     return a*b
#     if operator == "+":
#         return add
#     elif operator == "*":
#         return product
# sum = calculator("+")
# multiply = calculator ("*")
# print(sum(10,50))
# print(multiply(10,50))
    

# def calculator(operator,a,b):
#     def add():
#         return a+b
#     def product():
#         return a*b
#     if operator == "+":
#         return add
#     elif operator == "*":
#         return product
# a = calculator("+",10,15)
# b = calculator ("*",10,15)
# print(a())
# print(b())