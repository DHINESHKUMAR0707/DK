'''
def your(name):
    print("vanakkam",name)
your("DK")
#using return
def name():
    return "Dk"
a=name()
print("vanakkam",a)

#user defined function 
def add(a,b):
    return a+b
a=add(6,7)
b=add(10,50)
print(a)
print(b)

# scope in function
x=10
Y=20
def add():
    X=5
    Y=4
    return X+Y
Z=add()
print(Z)
def sub():
        X=5
        Y=4
        return X-Y
e=sub()
print(e)
def mul():
        X=5
        Y=4
        return X*Y
f=mul()
print(f)
def div():
        X=5
        Y=4
        return X/Y
d=div()
print(d)
#in built function in python
import random

print(random.randint(1, 10))  # Output: a random number from 1 to 10

import datetime

print(datetime.datetime.now())  # Output: current date and time

import os

print(os.getcwd())  # Get current working directory



print(dir(__builtins__))

import os

print(os.getcwd())  # Get current working directory

import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 6]

plt.plot(x, y)
plt.title("Line Chart")
plt.show()

text ="Python"
print(ascii(text))

def h(n):
    if n == 0:
        return 0
    return n + h(n - 1)
print(h(5))

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5))

def fact(n):
    if n == 0 :
        print("EVEN")
        return 1
    return n%2==0 
print(fact(5))
a=str(input())
b="g"
if a in b:
    c.count(a)
print(c)
'''
a=str(input())
b="g"
i=0
for  i in a:
    if i.lower() in a:
        i.count(b)
        i += 1
        print(i)