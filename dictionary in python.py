'''
# Dictionary Syntax
a={'name':'DHINESH KUMAR',
'age':'200',
'class':'First' }
print(a)
#Choosing key values
a={'name':'DHINESH KUMAR',
'age':'200',
'class':'First' }
print(a['age'])
#Duplicates in python
a={'name':'DHINESH KUMAR',
'age':'200',
'age':'200',
'class':'First' }
print(a)
#Same key values
a={'name':'DHINESH KUMAR',
'age':'200',
'age':'20',
'class':'First' }
print(a)

#example program
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
print(a)
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
print(a['name'],['Roll number'],['Department'],['College'],['Blood Group'])
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
print(a.values())

#methods in Dictionary
#length
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
print(len(a))
#Get keys
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
print(a.get('name'))
# get keys if not the value is present
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
print(a.get('Blood'))
#keys
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
print(a.keys())
#Values
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
print(a.values())
#Items
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
print(a.items())

#Copying Dictionary
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
b=a.copy()
print(b)
#values in copied dictionary
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
b=a.copy()
print(b.values())

#updating Dictionary
a={'name':'DHINESH KUMAR',
'Roll number':'22BM010',
'Department':'BME',
'College':'MEC',
'Blood Group':'0+Ve' }
a.update({'vazkai':'Goes on flow'})
print(a)

#Example based on a movie
retro={'Movie':'Retro',
        'Hero':'Surya',
        'Heroine':'Pooja',
        'Best song':'The one',
        'Best Scene':'Surya meets pooja after came from prison'
        }
#length of retro
print(len(retro))
#get key values of retro
print(retro.get('Hero'))
#get keys of retro
print(retro.keys())
#key values of retro
print(retro.values())
#items of retro
print(retro.items())
#copying retro
anjaan=retro.copy()
print(anjaan)
#updating retro
retro.update({'Best dialouge':'nee siricha alaga irukkum daa paari '})
print(retro)

#Practice Questions for dictionary
#1)create a dictionary to store the names and ages of 3 people.then print the dictionary.
a={'age of thambi':12,
   'age of rajan':20,
   'age of anbu':10}
print(a)
#2)Access the value of a specific key from a dictionary 
a={'age of thambi':12,
   'age of rajan':20,
   'age of anbu':10}
print(a.get('age of thambi'))
#3)Add a new key value pair to a dictionary
a={'age of thambi':12,
   'age of rajan':20,
   'age of anbu':10}
a.update({'age of guna':19})
print(a)
#4)update athe value of an existing key.
a={'age of thambi':12,
   'age of rajan':20,
   'age of anbu':10}
a.update({'age of thambi':15})
print(a)
#5)check if a key exists in a dictionary
a={'age of thambi':12,
   'age of rajan':20,
   'age of anbu':10}
print(a.get('age of chandra'))


#delete in dictionary
a={'age of thambi':12,
   'age of rajan':20,
   'age of anbu':10}
a.pop('age of thambi')
print(a)

#user input in dictionary
a={}
b=int(input())
for i in range(a):
   key=input("enter key ")
   value=input("enter value ")
   a[key]=value
print(a)

#loop in dictionary
a={'age of thambi':12,
   'age of rajan':20,
   'age of anbu':10}
print(a)
for key,values in a.items():
   print(key,":",values)
   '''
#user input and loop in dictionary
a={}
b=int(input())
for i in range(b):
   key=input("enter key ")
   value=input("enter value ")
   a[key]=value
   print(a)
for key,values in a.items():
   print(key,":",values)