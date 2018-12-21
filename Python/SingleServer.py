# -*- coding: utf-8 -*-
"""
Created on Sat May  5 10:41:12 2018

@author: User
"""

import random
print("\t\t\tSIMULATION PROJECT\n\n")
len=int(input("Enter Arrival time: "))

#arrival time random
vet = [random.randint(10,80) for _ in range(len-1)]
vet1 = [random.randint(10,80) for _ in range(len)]
arrRandom=[0]+vet
arrivalTime =[0]+ [random.randint(1,10) for _ in range(len-1)]
print("Random number of Arrival time")
for i  in range(len):
    print(arrRandom[i],end=",")
print("\n\nRandom number of Service time")
for i  in range(len):
    print(vet1[i],end=",")

print("\n\nTime Between Arrival Determination:")     
print("----------------------------------------------------------------------")
print("CustomerNumber |Random Digit | Time Between Arrival")
print("----------------------------------------------------------------------")

for line in range(0,len):
    print("\t|",line+1,"\t\t|",arrRandom[line],"\t\t|",arrivalTime[line])
print("----------------------------------------------------------------------")


#service time random
print("\n\nService Time Genarated:")     
print("----------------------------------------------------------------------")
print("CustomerNumber |Random Digit | Service Time")
print("----------------------------------------------------------------------")
serviceTime = [random.randint(1,10) for _ in range(len)]
for line in range(0,len):
    print("\t|",line+1,"\t\t|",vet1[line],"\t\t|",serviceTime[line])
print("----------------------------------------------------------------------")
print("\n\nSimulation Table:") 
print("----------------------------------------------------------------------")
print("A\t|B\t|C\t|D\t|E\t|F\t|G\t|H\t|I")
print("Number\t|TSLA\t|AT\t|ST\t|TSB\t|QL\t|TSE\t|CWS\t|ITOS")
print("----------------------------------------------------------------------")
L=0
LatArraival=[]
serviceTimeEnd=[]
spendInSystem=[]
customerspend=[]
idleTime=[0]+[]
TimeServiceBegin=[]
waitQueue=[0]+[]

for line in range(0,len):

     L+=arrivalTime[line]
     LatArraival.append(L)
     serviceTimeEnd.append(LatArraival[line]+serviceTime[line])
     spendInSystem.append(serviceTimeEnd[line]-serviceTime[line])
     customerspend.append(serviceTimeEnd[line]-LatArraival[line])
for line in range(0,len):
     for line1 in range(1,len):
         if(serviceTimeEnd[line1-1]>LatArraival[line1]):
             waitQueue.append(serviceTimeEnd[line1-1]-LatArraival[line1])
             serviceTimeEnd.append(waitQueue[line1]+LatArraival[line1])
         else:
             waitQueue.append(0)

     TimeServiceBegin.append(LatArraival[line]+waitQueue[line])
     

for line in range(0,len):
     for line3 in range(1,len):
         idleTime.append(TimeServiceBegin[line3]-serviceTimeEnd[line3-1])
      
     print(line+1,"\t|",arrivalTime[line],"\t|",LatArraival[line],"\t|",serviceTime[line],"\t|",TimeServiceBegin[line],"\t|",waitQueue[line],"\t|",serviceTimeEnd[line],"\t|",customerspend[line],"\t|",idleTime[line])
print("----------------------------------------------------------------------")