#class and object


# class Car: #property and function
#     #initialization function ma value haru initialize garnu paryo
#     def __init__(self, model, color):
#         self.model = model #rhs ma vako model chae function ko parameter bata aako ho
#         self.color = color #lhs ma object ko attribute ko value 

# c = Car("2022","black")
# print(c.model)
# print(c.color)


#noun -> object
#adjective -> attribute, property
#verb -> behavior, method


# book -> object, page -> attribute, read -> method
# class Book:
#     def __init__(self, page):
#         self.pagenum = page
#     def read(self):
#         print(f"page num {self.pagenum} is being read")
# b = Book(200)
# b.read()
# print(b.pagenum)


# class Page:
#     def __init__(self,pagenum,content):
#         self.pagenum = pagenum
#         self.content = content
#     def read(self): #instance method
#         print(f"Reading {self.content} of page number {self.pagenum}")
#     def __str__(self): #yo fn vayena vane 'this is new page ' print hunna
#         return self.content
#     def __repr__(self): #yo fn vayena vane list print hunna
#         return self.content
        

#     @staticmethod
#     def print_to_printer(content): #static method
#         print(f"Printing....")
#         print(content)
# # p = Page(1, "This is new paragraph ")
# # p.read()
# # Page.print_to_printer("This is sentence. ")


# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
#     def num_of_pages(self):
#         return len(self.pages)
#     def add_pages(self, page):
#         self.pages.append(page)
#     def __str__(self): #yo fn vayena vane maths print hunna 
#         return self.title
#     def get_content(self,pagenum):
#         for i in self.pages:
#             if i.pagenum == pagenum:
#                 return i.content
#         return "Page not found"



# pages = []
# for i in range(1,6):
#     p = Page(i, f"This is paragraph {i}")
#     pages.append(p)

# b = Book("Maths", pages)
# print(f"Number of pages = {b.num_of_pages()}")
# p = Page(6, "This is new page")
# b.add_pages(p)
# print(f"Number of pages = {b.num_of_pages()}")
# print(b)
# print(p)
# print(b.pages)
# print(b.get_content(5))
# print(b.get_content(10))
# print(b.__dict__)



try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
except ValueError:
    print("Can not convert into integer")
except NameError:
    print("Variable not defined")
else:
    print(n1+n2)