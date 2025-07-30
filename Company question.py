'''
a=int(input())
b=list(map(int,input().split()))
for i in  b:
    if b.count(i)==1:
     print(i)
     '''
#using XOR operator
a=int(input())
b=list(map(int,input().split()))
c=0
for i in  b:
    c^=i
print(c)