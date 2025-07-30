# check given integer is palindrome or not
a=list(map(int, input("Enter the value :").split()))
b=a[:]
a.reverse()
if a==b:
    print("It is a palindrom")
else:
    print("It is not a palindrom")
 # check given Alphabet is palindrome or not
a=list(map(str, input("Enter the value :").split()))
b=a[:]
a.reverse()
if a==b:
    print("It is a palindrom")
else:
    print("It is not a palindrom")
#sum of first n natural number.
a=list(map(int, input("Enter the value :").split())) 
print(sum(a))
#sum of first n natural number.   
a=list(map(int, input("Enter the value :").split())) 
print(sum(a))
# print all vowels present in a string
a=("a","e","i","o","u")
b=str(input("Type a word :"))
for i in a :
   if (i in b):
    print(i,end="")
# print our letters  present in a string
a=list(map(str, input("Enter the value :").split())) 
b=input("")
for i in a :
   if (i in b):
    print(i,end="")
    
# print  not our letters  present in a string
a=list(map(str, input("Enter the value :").split())) 
b=input("")
for i in b :
   if (i not in a):
    print(i,end="")

# print fibolicis series uo to n terms
a=input("Enter the number : ")
a,b=0,1
print("fibolicis series : ")
for i in range(a):
    print(i,end="")   
    a,b=b,a+b