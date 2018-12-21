
a=20
if(a==10):
    print("A is 10")
elif(a is 20):
    print("A is 20");
else:
    print("Not found!");
    


for a in range(0,10,2):
    print(a)
    
    for a in range(0,30,3):
        print(a)
        
        for a in range (0,40,4):
            print("rofi")
            
 
    
    number=5
while(number<10):
    print("number is:",number,"ok")
    print("number is:",number,number)
    number +=1;
    
    
    number=100
if(number<=100):
    print("Number less then 200");
    print("Really it it..")

print("Tata");




 

def bitcoin_to_dollar(btn):
    result=btn*100;
    print(result);
bitcoin_to_dollar(10)

def apurbas_limit(age):
    limit=age/2+7
    return limit
print(apurbas_limit(22))

def default_arg(sex="Unknown"):
    if(sex is "m"):
        print("Male")
    elif(sex is "f"):
        print("Female")
    else:
        print(sex);

default_arg("m");
default_arg("f");
default_arg();



def unpac(*arg):
    for name in arg:
        print(name)
lsname=["Apurba","Sifat","Hasan","Rafid"]
unpac(*lsname)


while True:
    try:
        x=int( ("Input your number:"))
        print(28/x)
        break
    except ValueError:
        print("Make sure and enter a number")
        break
    except ZeroDivisionError:
        print("Dont pic zero")
        break
    except:
        break
    finally:
        print("Loop Complete")
        
        
        player=[12,34,55,30,80];
print("player number is:%d"%player[2]+" ok");
player[2]=90;
print(player);

sec_number=[2,4,6,8,10];
for n in range(1,12):
    if(n in sec_number):
        continue;
    print(n);
    
    
    number=5
while(number<10):
    print("number is:",number,"ok")
    print("number is:",number,number)
    number +=1;
    
    number=100
if(number<200):
    print("Number less then 200");
    print("Really it it..")

print("Tata");


player.extend([130,140,150]);
print(player);

player.extend(range(10,15));
print(player);