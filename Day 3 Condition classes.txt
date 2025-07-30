# Decision Making Condition in python
'''
print("The Stored data in 22BM010 is DHINESHKUMAR")
print("The stored data in 22BM027 is NAVEENKUMAR")
print("The stored data in 22BM003 is ANANTH")
d=str(input("Give data to check  "))
print("The Given data is ",d)
a="22BM010"
a=d
b="22BM027"
b=d
c="22BM003"
c=d
if d is a:
 print("DHINESHKUMAR")
elif d is b :
    print("NAVVENKUMAR")
elif d is c:
    print("ANANTH")
else :
 print("The Given Value is not Stored")
 '''
'''
print("Pass Mark is 40 outoff 100.\n Your mark is >90 you are a topper")
a=40
b=int(input("Enter your mark "))
print("Your Mark is ",b)
if b>=40:
    print("You pass your Examination")
else:
    print("You are fail")
'''
'''
#TW and Fw questions :
a=int(input(" Enter the number of vechicles "))
print("Number of Vechicles is ",a)
b=int(input(" Enter the number of Wheels "))
print("Number of Wheels is ",b)
c=((a*4-b)//2)
if b<a and b<=a:
  print("Invalid Data")
else:
  print("Total number of Two wheeles is ",c)
  print("Total number of Four wheeles is ",a-c)
'''
'''

a=int(input("Enter your Mark "))
print("Entered Mark is ",a)
if 90<=a<=100:
  print(" Grade A")
elif 80<=a<=90:
  print(" Grade B")
elif 70<=a<=80:
  print(" Grade C")
else:
    print(" Fail ")

    
a=int(input("Enter a value "))
print("Entered value is ",a)
if ((a>=1 and a<=100)%a==1):
 print(" Weird ")
else:
    print(" Not Weird ")

a=int(input("Enter a value "))
if 2<=a<=5 and a%2==0:
  print(" Weird ")
else:
    print(" Not Weird ")
a=int(input("Enter a value "))
if 6<=a<=20 and a%2==0:
   print(" Weird ")
else:
    print(" Not Weird ")
a=int(input("Enter a value "))
if a<=20 and a%2==0:
  print(" Weird ")
else:
    print(" Not Weird ")
a=int(input("Enter a value "))
print("Entered value is ",a)
if a%4==0:
    print("Leap Year")
else:
    print("Usual year")

a=str(input("Choose your day "))
match a:
      case"Monday":
        print("Working day")
      case"Sunday":
        print("Leave day")
      case _:
        print("Working day")
'''

a=int(input("Enter your Mark "))
print("Entered Mark is ",a)
match a:
 case (a>=90):
  print(" Grade A")
 case (a>=80):
  print(" Grade B")
 case (a>=70):
  print(" Grade C")
 case _:
    print(" Fail ")
 






    

