'''
class a:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def addd(self,other):
        return a(self.x - other.x,self.y - other.y,self.z + self.z)    
    def string(self,others):
            return a(self.x + others.x,self.y +  others.y,self.z + others.z )
b=a(30,40,"D")
c=a(100,150,"k")
d=b.string(c)
print(d.x,d.y,d.z)

a=str(input("Enter a word"))
b=""
c=0
d=0
for i in a:
    if i.isupper():
     i=i.lower()
     c+=1 
    elif i.islower():
     i=i.upper()
     d+=1 
    else:
        print("Adhula onnum illa keela potrunga")

print(b)
print(c)
print(d)

z=["Even","Odd"]
a=int(input())
b=z[a%2]
print(b)
'''
class student :
    def __init__ (self,name,age):
        self.name=name
        self._age=age
        self.__grade="A"
    def get_grade(self):    
        return self.__grade
s=student("AKASH","Warning") 
print(s.name)
print(s._age)
print(s.get_grade())
