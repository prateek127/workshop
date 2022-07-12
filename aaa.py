"""a = [1,2,3,4,5]
for i in a:
    print(i)
    """

"""for i in range(1,10):
    if i%2==0:
        print (i)
"""
"""divisible =[]
nondiv =[]
for i in range(1,31):
    if i%3==0:
        divisible.append(i)
    else:
        nondiv.append(i)
print(divisible)
print(nondiv)"""

#print ("sum = ", sum(range(1,10)))



main =[]
even = []
odd = []
duplicates =[]

for i in range(1,10):
    n = int(input("Enter a num: "))
    if n not in main:
        if n%2==0:
            even.append(n)
        else:
            odd.append(n)
    else:
        duplicates.append(n)
    main.append(n)
print(main)
print(odd)
print(even)
print(duplicates)
