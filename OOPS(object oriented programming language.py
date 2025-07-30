
#OOPS(object oriented programming languange)
#class
class flight:
    Engine="Turbo Engine"
F=flight()
print(F.Engine)

#using __inint__ & self:
class bike:
    def __init__ (self,name,uniqueness,mileage,rate):
        self.name=name
        self.uniqueness=uniqueness
        self.mileage=mileage
        self.rate=rate
interstellar=bike("interstellar","high pump",35,350000)
belly=bike("belly","posture",20,250000)
ninja=bike("Ninja","Turbo Speed",15,1500000)
a=(str(input("Enter a bike name :")))
name1=interstellar.name
a1=(f"Bike_name :{interstellar.name},uniqueness :{interstellar.uniqueness},Mileage :{interstellar.mileage},Rate :{interstellar.rate}")
name2=belly.name
b1=(f"Bike_name :{belly.name},uniqueness :{belly.uniqueness},Mileage : {belly.mileage},Rate :{belly.rate}")
name3=ninja.name
c1=(f"Bike_name :{ninja.name},uniqueness :{ninja.uniqueness},Mileage :{ninja.mileage},Rate :{ninja.rate}")
if a == name1 :
    print(a1)
elif a == name2:
    print(b1)
elif a == name3:
    print(c1)
else:
    print("Invalid bike name")
#[[[[[[[[[[[[[[[[[[[[[[[

#add,sub,divide,muplit
import statistics
class marks:
    def __init__(self,maths,physics,chemistry):
        self.maths=maths
        self.physics=physics
        self.chemistry=chemistry
Ajith=marks(90,60,80)                                             #indeclared
Vijay=marks(70,67,88)
Surya=marks(88,75,65)
Dhanush=marks(85,55,65)
def average(a,b,c):
        return statistics.man
c=average(Ajith.maths,Ajith.physics,Ajith.chemistry)
print(c)

#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
