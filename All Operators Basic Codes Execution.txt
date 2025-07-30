
#operators
#Arithmatic Operators
print("_____________________________________________")
print("Arithmatic Operation")
print("_____________________________________________")
a=int(input(" Enter the value of A "))
print("The value of A = ",a)
b=int(input( " Enter the value of B "))
print("The value of B = ",b)     
print("Addition",a+b)
print("Subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Exponentiation",a**b)
print("Floor Division",a//b)
print("Modulus",a%b)
#Comparision Operators
print("_____________________________________________")
print("Comparision Operators")
print("_____________________________________________")
a=int(input(" Enter the value of A "))
print("The value of A = ",a)
b=int(input( " Enter the value of B "))
print("The value of B = ",b)     
print("A Equal to B",a==b)
print("A not Equal to B",a!=b)
print("A is Greater than B",a>b)
print("A is Lesser than B",a<b)
print("A is Greater than or Equal to B",a>=b)
print("A is Lesser thsn or Equal to B",a<=b)
#Assingment Operators
print("_____________________________________________")
print("Assingment Operators")
print("_____________________________________________")
a=int(input(" Enter the value of A "))
print(" The Value of A is ",a)
print("The Value A is Operationed By the Value X")
x=int(input("Enter the value of X "))
a+=x
print(a)
a-=x
print(a)
a*=x
print(a)
a/=x
print(a)
a**=x
print(a)
a//=x
print(a)
a%=x
print(a)
a/=x
print("_____________________________________________")
print("Logical Operator")
print("_____________________________________________")
#Logical Operator
a=int(input(" Enter the value of A "))
print("The value of A = ",a)
b=int(input( " Enter the value of B "))
print("The value of B = ",b)
a==b and b==a
print("A Equal to B and B",a==b and b==a)
a<b and b>a
print("A is Lesser than B and B is Greater than A",a<b and b>a)
a>b and b<a
print("A is Greater than B and B is Lesser than A",a>b and b<a)
a>b or b<a
print("A is Greater than B Or B is Lesser than A",a>b or b<a)
a<b or b>a
print("A is Lesser than B Or B is Greater than A",a<b or b>a)
a>b or b<a
print("A is Greater than b Or B is Lesser than A",a>b or b<a)
not a>b
print("A is  Lesser than B",not a>b)
not b<a
print("B is Greater than A",not b<a)
not a==b
print("A is Not Equal than B",not a==b)
not b<=a
print("B is Greater than Or Equal A to",not b<=a)
not a>=b
print("A is Lesser than Or Equal to B",not a>=b)
print("_____________________________________________")
print("Bitwise Operator")
print("_____________________________________________")
#Bitwise Operator
a=int(input(" Enter the value of A "))
print("The value of A = ",a)
b=int(input( " Enter the value of B "))
print("The value of B = ",b)
a&b
print("The AND Operation for  A and B is ",a&b)
a|b
print("The OR Operation for A and B is ",a|b)
a^b
print("The XOR Operation for A and B is",a^b)
~a
print("The NOT Operation for A is",~a)
~b
print("The NOT Operation for B is",~b)
a<<b
print("The Left Shift Operation for A and B is",a<<b)
a>>b
print("The Right Shit operation for A and B is",a>>b)
print("_____________________________________________")
print("Membership Operator")
print("_____________________________________________")
#Membership Operator
print("The Stored data is 07,04,09,09,10,11")
a="07,04,09,09,10,11"
b=(input( " Give Data to Check  "))
b in  a
b not in a
print("Given data is present in Stored data ",b in a)
print("Given data does not present in Stored data ",b not in  a)
print("_____________________________________________")
print("Membership Operator using Ifelse condition")
print("_____________________________________________")
#Membership Operator using Ifelse Condition 
print("The Stored data is 07,04,09,09,10,11")
a="07,04,09,09,10,11" 
b=(input( " Give Data to Check  "))
print(" Given Data to check ",b)
if b in a:
  print("Data Were Stored")
elif b not in  a:
  print("Data Were Not Stored")
print("_____________________________________________")
print("Identify Operator using Ifelse condition")
print("_____________________________________________")
#Identify Operator
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




      




      
