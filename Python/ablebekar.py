class Caller():
    
    interArrivalTime = 0
    arrivalTime = 0
    whenAbleAvailable = 0
    whenBakerAvailable = 0
    serverChosen = 0   # 0 is able and 1 is baker
    serviceTime = 0
    timeServiceBegins = 0
    ableServiceCompletedTime = 0
    bakerServiceCompletedTime = 0
    callerDelay = 0
    timeInsystem = 0
    
    
     def __init__(self,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11):
        self.interArrivalTime = i1
        self.arrivalTime = i2
        self.whenAbleAvailable = i3
        self.whenBakerAvailable = i4
        self.serverChosen = i5
        self.serviceTime = i6
        self.timeServiceBegins = i7
        self.ableServiceCompletedTime = i8
        self.bakerServiceCompletedTime = i9
        self.callerDelay = i10
        self.timeInsystem = i11
        from caller import *
import random

def getInterArrivalTime(customerList):
    return random.choice(customerList)
def getAbleOrBaker(ableAvailTime,bakerAvailTime,priority):
    if(ableAvailTime == bakerAvailTime):
        if(priority == 2):
            select = random.choice([0,1])
            return select
        else:
            return priority 
    else:
        if(ableAvailTime < bakerAvailTime):
            return 0
        else:
            return 1    
def getServiceTime(ableOrBaker,ableList,bakerList):
    if(ableOrBaker == 0):
        return random.choice(ableList)
    else:
        return random.choice(bakerList)

def customerGenerator(customerTimeList,ableList,bakerList,priority,customerOrTime,count):
    
    customerList = list()
    
    if(customerOrTime):
        for i in range(count):
            if(len(customerList) == 0):    # The fist caller
                if(priority == 2):
                    priority  = random.choice([0,1])
                if(priority == 0):
                    servTime = random.choice(ableList)
                    customerList.append(Caller(0,0,0,0,0,servTime,0,servTime,0,0,0))
                if(priority == 1):
                    servTime = random.choice(bakerList)
                    customerList.append(Caller(0,0,0,0,1,servTime,0,0,servTime,0,0))                
            else:
                interArrVlTime = getInterArrivalTime(customerTimeList)
                timeInSystem = customerList[len(customerList)-1].arrivalTime
                if(priority == 2):
                    priority  = random.choice([0,1])
                ableBaker = getAbleOrBaker(customerList[len(customerList)-1].ableServiceCompletedTime, customerList[len(customerList)-1].bakerServiceCompletedTime, priority)
                servTime = getServiceTime(ableBaker, ableList, bakerList)
                
                if(ableBaker == 0):                    
                    arrivalTime = customerList[len(customerList)-1].arrivalTime + interArrVlTime
                    whenAbleAvailable = customerList[len(customerList)-1].ableServiceCompletedTime
                    whenBakerAvailableTime = customerList[len(customerList)-1].bakerServiceCompletedTime
                    
                    if(arrivalTime > whenAbleAvailable):
                        whenServiceBegins = arrivalTime
                    else:
                        whenServiceBegins = whenAbleAvailable
                    
                    if(arrivalTime < whenServiceBegins):
                        delay = whenServiceBegins - arrivalTime
                    else:
                        delay = 0 
                    customerList.append(Caller(interArrVlTime,arrivalTime,whenAbleAvailable,whenBakerAvailableTime,0,servTime,whenServiceBegins,whenAbleAvailable + servTime,whenBakerAvailableTime,delay,timeInSystem))
                if(ableBaker == 1):
                    arrivalTime = customerList[len(customerList)-1].arrivalTime + interArrVlTime
                    whenAbleAvailable = customerList[len(customerList)-1].ableServiceCompletedTime
                    whenBakerAvailableTime = customerList[len(customerList)-1].bakerServiceCompletedTime
                    
                    if(arrivalTime > whenBakerAvailableTime):
                        whenServiceBegins = arrivalTime
                    else:
                        whenServiceBegins = whenBakerAvailableTime
                    
                    if(arrivalTime < whenServiceBegins):
                        delay = whenServiceBegins - arrivalTime
                    else:
                        delay = 0        
                    customerList.append(Caller(interArrVlTime,arrivalTime,whenAbleAvailable,whenBakerAvailableTime,1,servTime,whenServiceBegins,whenAbleAvailable,whenBakerAvailableTime + servTime,delay,timeInSystem))
    else:
        pass
    
    return customerList   
    from dataProcessing import *  
from textTester import *                

def main():
    
   #Input data ->Mahdi
    customerInterArrivalTime = [1,2,3,4]  
    ableServiceTime = [5,6,7,8] 
    bakerServiceTime = [10,11,12,13] 
    ableBakerPriority = 0 #If 0 => Able is first if 1 => baker is first if 2 => randomly chosen
    
    selectCustomerOrTime = True #If true customer number is given if false time period is given
    
    customerCount = 100  
    timeLength = 0 
    
    
    
    # Data processing  -> MrHs
    if(selectCustomerOrTime):
        count = customerCount
    else:
        count = timeLength
    lili = customerGenerator(customerInterArrivalTime, ableServiceTime, bakerServiceTime, ableBakerPriority, selectCustomerOrTime, count)
    
    
    # printing output using django -> Mahdi
    
    test(lili)
    
    return 0

main()
