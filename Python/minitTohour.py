def minites_to_hours(minites):
    hours=minites/60
    return hours
print(minites_to_hours(700))
---------------------------------------
age = int(input("Enter age: "))
new_age=float(age)+40
print(new_age)

----------------------------------------------
def age_foo(age):
    new_age=float(age)+50
    return new_age
age=input("Enter age: ")
print(age_foo(age))
--------------------------------------
a=int(input("Enter The Number: "))

if a%2==0:
   print("The Number is Even ")
else:
    print("The Number is Odd")
-----------------------------------------------------------
emails=['you@gmail.com','i@hotmail.com','you@yahoo.com'] 
for item in emails:
    if 'gmail' in item:
        print(item)
----------------------------------------------------------
     
mylist=[1,2,3,4,5,6]
for item in mylist:
    print(item)
--------------------------------------------------------------    
list=[1,2,3,4,5,6]
for item in list:
    if item>2:
        print(item)
-----------------------------------------------------
def currency_convert(rate,eurro):
    dollar=rate*eurro
    return dollar
r=float(input("Enter Rate: ") )
e=float(input("Enter Eurro: ") )  
currency_convert(r,e) 
print(currency_convert(float(r) ,float(e))) 
-------------------------------------------------------

password=''
while password != 'python123':
    password=input("Enter Your Passowrd: ")
    if password=='python123':
        print("Welcome, Successfully login! ")
    else:
        print("Pleas try again!")



import numpy as np
 
n= np.arange(27)
print(n)

n.reshape(3,3,3 )

import cv2
im=cv2.imread("IMG.jpg",1)
print(im)







