#DSA in python
#O(1)
a=10
b-18
print(a+b)
#o(n)
a=int(input(""))
if a%2==0:
    print("EVEN")
elif a%2==1:
    print("ODD")
#o(log n)
a=int(input())
b=int(input())
for i in range(a):
    for j in range (b):
        if j==0 or i==a-1:
           print("*",end="")
        else:
           print("",end="")
    print()
#o(n2)
a=int(input())
b=int(input())
for i in range(a):
    for j in range (b):
        if j==0 or i==a-1:
           print("*",end="")
        else:
           print("",end="")