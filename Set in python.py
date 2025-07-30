'''
a={1,2,3}
print(a)
# LOOP IN SET
a=set(str, input("Enter the value :").split())
b=input("")
for i in b :
   if (i not in a):
    print(i,end="")
#methods
a={100,200,300,400}
a.add(1000)
a.remove(100)
a.discard(1)
print(a)

#operations in set
a=set(map(int, input("Enter the value A :").split()))
b=set(map(int, input("Enter the value B :").split()))
print(a)
print(b)
c=a|b #
print(c)
d=a&b
print(d)
e=a-b
print(e)
f=a^b
print(f)

