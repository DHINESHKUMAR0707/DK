
#Tuple
a=()
b=(123,"DK",3.4)
c=(1,2,3,4,5,6,7,8,9,)
d=("c",)
print(a)
print(b)
print(c)
print(d)
#Tuple indexing
c=(1,2,3,4,5,6,7,8,9,)
a=c[2]
print(a)
a=c[1:4]
print(a)
a=c[4]
print(a)
#Tuple negative indexing
c=(1,2,3,4,5,6,7,8,9)
a=c[-2]
print(a)
a=c[-1:-4]
print(a)
a=c[-4]
print(a)
#Tuple operator 
a=list(map(int, input("Enter the value :").split()))
b=list(map(int, input("Enter the value :").split()))
print(a+b)
print(a*5)
print(a[5])
print(b[6])
print(a[2:5])
print(b[3:8])
print(2 in a)
print(2 not in a)
print(10 in b)
print(10 not in b)
#add or remove in tuple
a=list(map(int, input("Enter the value :").split()))
a[3]

#interating tuple
a=list(map(int, input("Enter the value :").split()))
print("Idhu ellam a variable la irukku\n")
for i in a:
    print(i)
    
# Tuple functions or methods
a=tuple(map(int, input("Enter the value :").split()))
print("Lenght of the a:",len(a))
a=tuple(map(int, input("Enter the value :").split()))
print("Maximum value of the a:",max(a))
a=tuple(map(int, input("Enter the value :").split()))
print("Minimum value of the :",min(a))
a=tuple(map(int, input("Enter the value :").split()))
print("Sum of a:",sum(a))
a=list(map(int, input("Enter the value :").split()))
print("Tuple a:",tuple(a))
a=tuple(map(int, input("Enter the value :").split()))
print("sort of a:",sorted(a))
a=tuple(map(int, input("Enter the value :").split()))
cnt=a.count(2)
print("2 Count in a is ",cnt)

a=tuple(map(int, input("Enter the value :").split()))
ind=a.index(2)
print("Index of 2 is ",ind)