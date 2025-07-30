'''a=int(input("enter the number "))
for i in range(a):
    for j in range(i):
     print("*",end="")
    print("")
a=int(input())
for i in range(1,a+1):
     print("*"*i)
a=int(input())
for i in range(a):
     print("*"*i)
a=int(input())
for i in range(a,0,-1):
     print("*"*i)'''
a=int(input())
b=int(input())
for i in range(a):
    for j in range (b):
        if j==0 or i==a-1:
           print("*",end="")
        else:
           print("",end="")
    print()