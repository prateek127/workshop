print("Hello its subtraction time")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def subtraction(a,b):
    if a>b:
        print(a-b)
    else:
        print(b-a)
subtraction(a,b)