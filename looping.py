#for <variable> in <iterable>:
    #body
"""a = [1, 2, 3]
for i in a:
    n = input("Enter number: ")
    print(n)"""



"""sum = 0
for i in range(1,20):
    sum = sum + i
    #print("sum of  = ", sum)
    print(f"({i}. sum = {sum})")
"""


"""even = []

for i in range(10):
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        even.append(n)
print (even)
"""


"""nums =[]
for i in range(50):
    if i % 3 == 0:
        nums.append(i)
print(nums)
"""
"""print ("sum using range = ", sum (range(1,15)))
alist = [i for i in range(1,51)]
print ("alist = ",alist)
blist = [i for i in range(1,51) if i%3 == 0]
print("blist = ", blist)"""


"""
main = []
even = []
odd = []
duplicate = []

for j in range(8):
    i = int(input("Enter a number: "))
    main.append(i)
    if(i%2) == 0:
        even.append(i)
        if even.count(i) != 1:
            even.remove(i)
            duplicate.append(i)
    if(i%2) == 1:
        odd.append(i)
        if odd.count(i) != 1:
            odd.remove(i)
            duplicate.append(i)
print ("main = ", main)
print ("even = ", even)
print ("odd = ", odd)
print("duplicate = ", duplicate)

"""
"""
main = []
even = []
odd = []
dup = []
for i in range(10):
    user = int(input("enter number:"))
    if user not in main:
        if user%2 == 0:
            even.append(user)
            print(even)
        else:
            odd.append(user)
            print(odd)
    else:
        dup.append(user)
        print(dup)
    main.append(user)"""


"""sum = 0
n = "12d34d56d78"
a = (n.split("d"))
print (a)
for i in a:
    sum = sum + int(i)
print (sum)
"""
# mathiko code ko single line code
"""total = 0
n = "12d34d56d78"
total = sum([int(i) for i in n.split("d")])
print(total)"""

"""
sum = 0
for i in range(50):
    if i%4 == 0:
        print(i)
        sum = sum + i
print(sum)
"""

total = 0
total = sum(int (i) for i in range(50) if i%4==0)
print (total)

print("sum = ", sum(range(4,51,4)))
