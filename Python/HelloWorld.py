from pip._vendor import requests
from pip._vendor.distlib.compat import raw_input
from collections import Counter
from operator import attrgetter
import Module
import heapq
import random
import threading
import urllib.request
import requests
from bs4 import BeautifulSoup
print("Hello World!");
print("Oh Ya,it's running..");
print("Hi i'm Apurba");
Name="Apurba";
print(Name*5);
a=3;
b=a**3;
print("Ans is:%d"%(b));
#Slicing string
string="I am a Student";
print(string[0]);
print(string[7]);
print(string[-1]);
print(string[-7]);
print(string[2:8]);
print(string[0:8]);
print(string[-7:0]);
print(len(string));
#List
player=[12,34,55,30,80];
print("player number is:%d"%player[2]+" ok");
player[2]=90;
print(player);
#temporary add list member
x=player+[10,20,30];
print(x);
print(player);
#Add value parmanentaly in List
player.append(120);
print(player);
player[:2]=[0,0];
print(player);
player[:2]=[];
print(player);
#Add multi value in list
player.extend([130,140,150]);
print(player);
#Add multi value by range in list
player.extend(range(10,15));
print(player);
#if else condition
number=100
if(number<200):
    print("Number less then 200");
    print("Really it it..")

print("Tata");
#anonter example of if else
a=20
if(a==10):
    print("A is 10")
elif(a is 20):
    print("A is 20");
else:
    print("Not found!");

#for loop
for a in range(1,10,2):
    print(a)

#for loop another example
list=["mango","banana","apple","guava","orange"];
for fname in list:
    print(fname);
    if(fname is "apple"):
        break;

#while loop
number=5
while(number<10):
    print("number is:",number,"ok")
    print("number is:",number,number)
    number +=1;
#another use for
sec_number=[2,4,6,8,10];
for n in range(1,12):
    if(n in sec_number):
        continue;
    print(n);
#Function
def call():
        print("Function is calling");
call()
def bitcoin_to_dollar(btn):
    result=btn*100;
    print(result);
bitcoin_to_dollar(10)

def apurbas_limit(age):
    limit=age/2+7
    return limit
print(apurbas_limit(22))
#default value for argument
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
#keyword argument
def testing(name="Apurba",work="ate",item="toona"):
    print(name,work,item)
testing()
testing(item="book",work="read")
#flexiable number of argument
def flexible(*arg):
    total = 0;
    for i in arg:
        total+=i;
    print(total)
flexible(10)
flexible(3,10,1000)
# Unpacking Arguments
def unpac(*arg):
    for name in arg:
        print(name)
lsname=["Apurba","Sifat","Hasan","Rafid"]
unpac(*lsname)
#walmart and set
set={"mango","rice","floor","oil","chicken"}
if "mango" in set:
    print("you already have mango");
else:
    print("oh ya you need mango");
'''
#User input string
name = raw_input("please input your name:\n")
print(name)
#User input integer
age = input("What is your age? ")
print(age)
'''
#Dictionary
set={"On":"Open something","Off":"Close Something","Good":"Telling about positive"}
print(set)

for key,value in set.items():
    print(key,value)

#using dictionary
name = raw_input("search:\n")
if name in set:
    print(set[name])
else:
    print("Not found!")

#Module and Random number
Module.open()
x=random.randrange(1,1000)
print(x)

#Download image from the internate
def download_image(url):
    x = random.randrange(1, 1000)
    fullname=str(x)+".jpg"
    urllib.request.urlretrieve(url,fullname)

#download_image("https://drive.google.com/file/d/1g46aGPT3_R2MDMLf2EdzhO_S8AeWonsKLQ/view")

#File write and read
fw=open("test.text","w")
text = raw_input("Write in file::\n")
fw.write(text)
fw.close()

fo=open("test.text","r")
text=fo.read()
print(text)
fo.close()

#Request website through python
'''
def trade_spider(max_pages):
    page=1
    plain_text=""
    while page<=max_pages:
        url='http://it-ebooks.directory/page-2.html?'
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'blh'}):
            href = "http://schema.org/Book" + link.get('href')
            #title = link.string  # just the text, not the HTML
            print(href)
            #print(title)
            # get_single_item_data(href)
        page +=1
trade_spider(1)
'''
#Exception
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

#class and object
class test:
    life=3
    def attack(self):
        print("ouch")
        self.life-=1
    def lifecycle(self):
        print("Life is:",self.life)
object = test()
object1 = test()
object.attack()
object.attack()
object.lifecycle()
object1.lifecycle()

#__init__ in python
class init:
    def __init__(self):
        print("When object is created, automatically call this function")
    def print(self):
        print("ok baby..")
obj=init()
obj.print()

class init1:
    def __init__(self,x):
        self.value=x
    def print(self):
        print(self.value)
ob=init1(10)
ob.print()

#class vs instance variable
class classVSinstance:
    gender="female"
    def __init__(self,name):
        self.name=name

obj1=classVSinstance("Susmita")
obj2=classVSinstance("Protiva")
print(obj1.name)
print(obj1.gender)
print(obj2.name)
print(obj2.gender)

#Inheritance in Python
class base():
    def last_name(self):
        print("Daria")
class drive(base):
    def first_name(self):
        print("Apurba")
base_obj=drive()
base_obj.first_name()
base_obj.last_name()

#Multipale inheritance
class mash:
    def production(self):
        print("Ya its ready")
class room:
    def pacate(self):
        print("pacation is ready")
class mashroom(mash,room):
    pass#if we want to skip define class we can use pass keyword
mas_room_obj=mashroom()
mas_room_obj.production()
mas_room_obj.pacate()

#Threading
class thread(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
obj1=thread()
obj2=thread()
obj1.start()

obj2.start()

#Word Frequency Counter
'''
def start(url):
    word_list=[]
    source_code=requests.get(url).text
    soup=BeautifulSoup(source_code)
    soup(url, "html.parser")
    for post_text in soup.findAll('a',{'class':'post-text'}):
        content=post_text.string
        #for result  in content:
        print(content)
start("https://stackoverflow.com/questions/4420563/ide-for-django-web-development")
'''
#Unpack list or tuples
date,name,price=["December 23,2015","Bread Gloves",8.51]
print(name)

def drop_first_last(grades):
    first,*middle,last=grades
    avg=sum(middle)/len(middle)
    print("Ans is:",avg)

drop_first_last([55,58,76,54,21])
drop_first_last([55,58,76,54,21,80,88,90,100])

#Zip in python
first=["Bucky","Tom","Taylor"]
last=["Roberts","Mank","Swift"]
names=zip(first,last)
for a,b in names:
    print(a,b)

#Lambda
answer=lambda x:x*7
print("Lambda Answer:",answer(5))

#Min Max and sorting Dictionary
stocks={"Goog":520.54,"FB":76.45,"Yahoo":39.28,"Amzn":308.21,"Appl":99.80}
print(sorted(zip(stocks.values(),stocks.keys())))
print(min(zip(stocks.values(),stocks.keys())))
print(max(zip(stocks.values(),stocks.keys())))

#map
'''
income=[10,30,75]
def double_money(dollars):
    return dollars*2

print(list(map(double_money,income)))
'''
grades=[32,43,654,34,132,66,99,580]
ans=heapq.nlargest(3,grades)
for res in ans:
    print(res)
#Finding Most Frequent Items

text="They are well done and I was moving along swimmingly until lesson 25.I had a couple of issues that I resolved by importing requests and BeautifulSoupdd" \
     "swimmingly until lesson 25.I had a couple of issues that I resolved by importing requests and BeautifulSoup swimmingly until lesson 25.I had a couple of" \
     "issues that I resolved by importing requests and BeautifulSoupbut I cannot open the url referenced in the videos"
words=text.split()
for wo in words:
    print(wo)
counter=Counter(words)
top_three=counter.most_common(3)
print(top_three)

#Sorting Custom Object
class User:
    def __init__(self,x,y):
        self.name=x
        self.user_id=y

    def __repr__(self):
        return self.name+ " : "+str(self.user_id)

users=[
    User("Bucky",4),
    User("Sifat",5),
    User("Hasan",90),
    User("Rafid",100),
    User("Apurba",80)
        ]
for user in users:
    print(user)

print("............")
for user in sorted(users,key=attrgetter("name")):
    print(user)

print("............")
for user in sorted(users,key=attrgetter("user_id")):
    print(user)


    '''
    Ok Python now I am tasted your flaver..
    Let's start django..
    '''