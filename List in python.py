
a=[10,"apple",3.15,True]
b=a[3]
print(b)

fruits=["apple","banana","cheery","orange"]
print(fruits[2])


a=[1,2,3,4,5,6,7,8,9]
b=[10,11,12,13,14,15,16,17,18]
print(a)
print(b)
a.append(11)
print(a)
b.extend([6,7])
print(b)
a=[1,2,3,4,5,6,7,8,9]
a.insert(6,10)
print(a)
a=[1,2,3,4,5,6,7,8,9]
a.remove(4)
print(a)
a=[1,2,3,4,5,6,7,8,9]
a.pop(5)
print(a)
a=[1,2,3,4,5,6,7,8,9]
a.clear()
print(a)
a=[1,2,3,4,5,6,7,8,9]
print("index")
print(a[1])
a=[1,2,3,4,5,6,7,8,9]
a.count(7)
print(a)
a=[1,2,3,4,5,6,7,8,9]
a.sort()
print(a)
a=[1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)
a=[1,2,3,4,5,6,7,8,9]
a.copy()
print(a)

#15.07.2025
#map
num=list(map(int, input("Enter the value :").split()))
result=list(map(lambda x:x%2==1,num))
print(result)
#filter 
num=list(filter(int, input("Enter the value :").split()))
result=filter(map(lambda x:x%2==1,num))
print(result)

#nested list 
a=[[5,7,8],[4,7,10],[10,11,15]]
b=a[2][1]
print(b)

#using for loop
a=list(map(int, input("Enter the value :").split()))
for i in a:
     print(i)
#list Questions
#create a list and print it.
a=list(map(int, input("Enter the value :").split()))
print(a)
#Access a 3rd element from the list and print it.
a=list(map(int, input("Enter the value :").split()))
b=a[3]
print(b)
# print the last integer of the list using negative indexing.
a=list(map(int, input("Enter the value :").split()))
b=a[-1]
print(b)
#change the value of the second item in a list.
a=list(map(int, input("Enter the value :").split()))
a.insert(2,10)
print(a)
#add a new element to the end of the list using append()
a=list(map(int, input("Enter the value :").split()))
a.append(11)
print(a)
#insert a element in index 2
a=list(map(int, input("Enter the value :").split()))
a.insert(2,10)
print(a)
#Remove a sepcific element from the list
a=list(map(int, input("Enter the value :").split()))
a.remove(2)
print(a)

#Delete the last element
a=list(map(int, input("Enter the value :").split()))
a.pop()
print(a)
#Sort the  lin ascending order.
a=list(map(int, input("Enter the value :").split()))
a.sort()
print(a)
#Reverse the list
a=list(map(int, input("Enter the value :").split()))
a.reverse()
print(a)

#join a list into another list
a=list(map(int, input("Enter the value :").split()))
b=list(map(int, input("Enter the value :").split()))
print(a+b)
