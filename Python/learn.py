# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 22:01:50 2018

@author: User
"""

a=5
b=5
c=a+b
print (c)

2==3



a=5
b=2
c=a//b
print(c)




name_list=["rofi" ,"Kawsar" ,"shanto" ,"ahad", "nahid" ,"sifat"]

name=input("Enter Name: ")


if name in name_list:
    print("He is may friend")
else:
    print("He is not may friend")
    
marke=input("Enter Your Number: ")
marke=int(marke)

if marke>=80:
    grad="A+"
elif marke>=70:
    grad="A"
elif marke>=60:
    grad="B"
elif marke>=50:
    grad="C"
elif marke>=40:
    grad="D"
else:
    grad="F"
    
print("Your grad: ", grad)

year=input("The Year: ")
year=int(year)

if year % 100 != 0 and year % 4 == 0:
    print("Yes")
elif year % 100 == 0 and year % 400 == 0:
    print("Yes")
else:
    print("No")

while password!=123:
   
    password=input("Enter your password: ")
    if password==123:
        print("Yes,wlcome")
    else:
        print("Try agin")