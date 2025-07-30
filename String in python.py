'''
#String in python
a="I'm Iron man"
print(a[2])
#methods in string
a=" I'm iron man"
print(a.upper())
print(a.lower())
print(a.title())
print(a.strip())
print(a.replace("a","e"))
print(a.count("m"))
print(a.find("man"))
b=['c','a','p','t','a','i','n','a','m','e','r','i','c','a']
print("_".join(b))
c="c,a,p,t,a,i,n,a,m,e,r,i,c,a"
print(c.split("_"))\
'''
#pratice questions
#1)reverse string
a=" I'm iron man"
print(a[::-1])
#2)check if a string is a palindrom
a="dad"
b=a[:]
a[::-1]
if a==b:
    print("It is a pallindrom")
else:
    print("It is not a pallindrome")
#3)find the lenght of the string without using len()
a=" I'm iron man"
count=0
for _ in a:
    count+=1
print(count)
#4)Replace all spaces with hypens
a=" I'm iron man"
print(a.replace(" ","-"))
#5)convert the first character of each word to uppercase
a=" I'm iron man"
print(a.title())
#6)print ASCII value for each character
a=" I"
print(ord(a[0]),ord(a[1]))
#7)remove all digits from string
a=" I'm1iron2man"
r=" "
for i in a:
    if not i.isdigit():
        r+=i
print(r)
#8)check if two strings are anagram
a="angle"
b="angel"
if sorted(a)==sorted(b):
    print("anagram")
else:
    print("not anagram")
#10)count words in a string
a=" I'm iron man"
print(a.count("I'm iron man"))