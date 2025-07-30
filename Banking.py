
class bank:
    def __init__ (self,username,pinnumber,balance):
         self.username=username
         self.pinnumber=pinnumber
         self.balance=balance
name1=bank("Dhineshkumar",7070,5000)
name2=bank("Ananth",2218,10000)
name3=bank("Naveenkumar",9925,15000)

a1="English"
a2="Hindi"
a3="tamil"
print(a1)
print(a2)
print(a3)
a6=str(input("Choose your language : "))
if a6 == a1:
    print("Choosing English")
elif a6 == a2:
    print("You have to choose English")
elif a6 == a3:
    print("You have to choose English")
else:
    print("Invalid language") 
a7=str(input("Choose your language : "))
if a7 == a1:
    print("Choosing English")
elif a7 == a2:
    print("You have to choose English")
elif a7 == a3:
    print("You have to choose English")
else:
    print("Invalid language") 
b1=str(input("Enter your pin number : "))
if b1 ==  name1.pinnumber :
    print("Welcome Dhineshkumar")
elif b1 == name2.pinnumber:
    print(" Welcome Ananth")
elif b1 == name3.pinnumber:
    print("Welcome Naveenkumar")
else:
    print("Account Not found")
