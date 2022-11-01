#def askAge():
#    age = int(input("Please enter in your age: "))
#    return age

#upper = askAge()

#for upper in range (upper, upper+21):
#    print(f"Your age is {upper}")

#info = []

#info.append = input("please enter in your name: ")
#info.append = input("please enter in your age: ")
#info.append = int(input("please enter in a number: "))
#print(info)

#number = [2,34,5,22,12,65]
#print(number)
#for i in (number):
#    print(i**2)

#list1 = ["i","your","dude"]
#list2 = ["am","boss","."]
#m = 0

#for i in list1:
#    print(i, list2[m], end=" ")
#    m += 1
"""
def createlist():
    list1 = []
    list2 = []
    list3 = []
    test = 0
    for i in range (0,5):
        test = input("Please enter an ineger value for list 1: ")
        if test.isdigit() == True:
            test = int(test)
            list1.append(test)
        else:
            print("Please enter a integer not a string")
        test = input("Please enter an ineger value for list 2: ")
        if test.isdigit() == True:
            test = int(test)
            list2.append(test)
        else:
            print("Please enter a integer not a string")

    for i in range (0,5):
        list3.append(list1[i] + list2[i])
    print(list3)
createlist()
"""

""" familymembers = []
rank = []
count = 0
run = 0
familymembers.append(input("Please enter a family member 1: "))
familymembers.append(input("Please enter a family member 2: "))
familymembers.append(input("Please enter a family member 3: "))
print("Please give your family members a ranking from 1 - 3")
while count < 3:
    rank.append(int(input(f"What rank would you give {familymembers[count]}: ")))
    count += 1
print("===========Ranking=======")
while run < 3:
    print(f"\t{familymembers[run]} - {rank[run]} ")
    run += 1 """

""" 
fname = input("Please enter in your first name: ")
lname = input("Please enter in your last name: ")
age = int(input("Please enter in your age: "))

info = {}
info[fname] = [lname, age]
print(info) """

""" player = {}
average = 0
sum = 0

for i in range (0,5):
    inputplayer = input("Please enter in your player: ")
    goals = int(input("Please enter in how many goals they scored so far: "))
    player[inputplayer] = goals
for i in player:
    sum += player[i]

average = sum/len(player)
print(average) """

""" def test (dic, testing):
    dup = False
    for i in dic:
        if i == testing:
            dup = True
            return True
    if dup == False:
        return False """

#file = open("file name", "r") r = read, w = write
#file.close() make sure to close or can hog memory
#with open("file name", w) as f:
    #f.write(variable) overwrites any current data
#data = file.read().splitlines() takes the data in the file and assigns it to a variable 

""" import random

rannumber = []
for i in range (0,100):
    rannumber.append(random.randint(1,100))
with open("C:\\Users\\ethan\\Desktop\\CIS  121\\Test.txt","w") as f:
    for i in rannumber:
        f.write(str(i) +"\n")
"""

""" def numbercheck(data):
    count = {}

    for i in data:
        if i in count:
            pass
        else:
            count[i] = data.count(i)
    return count

with open("C:\\Users\\ethan\\Desktop\\CIS  121\\Test.txt","r") as f:
    datalist = f.read().splitlines()    

with open("C:\\Users\\ethan\\Desktop\\CIS  121\\Test2.txt","w") as f:
    for key, value in numbercheck(datalist).items(): 
        f.write(f"{key}:{value})
 """
""" import random
 
def getnumber():
    numberdic = {}
    for i in range (1,11):
        number = int(input("Please enter a number 1-100: "))
        numberdic[f"Number {i}"] = number
    return numberdic

def guessnumber(numlist):
    guess = random.randint(1,100)
    for i in numlist.values():
        if i == guess:
            print(f"The computer gussed the number right! It was {i}")
        else:
            print("computer guessed the number wrong")

guessnumber(getnumber()) """

""" def listcombiner (keylist, valuelist):
    dic = {}
    for i in range (0,len(keylist)):
        dic[keylist[i] ]= valuelist[i]
    return dic

list1 = [1,2,3,4,5,6,7,8,10]
list2 = [5,4,3,2,1,4,5,6,1]

combinedlist = listcombiner(list1,list2)
print(combinedlist) """


""" def testvalue(number):
    if str(number).isdigit():
        return int(number)
    else:
        try:
            float(number)
            return float(number)
        except ValueError:
            return False


def multiply(dic,multiplyer):
    finished = []
    for i in dic:
        if testvalue(dic[i]) != False:
            finished.append(testvalue(dic[i])*multiplyer)
    return finished
test = {"A" : "e"}
test["a"] = "3"
test ["b"] = 5
print(multiply(test, 2)) """

""" import random

def randomlist(run):
    list1 = []
    list2 = []
    for i in range (0,run):
        list1.append(random.randint(0,1000))
        list2.append(random.randint(0,1000))
    return list1, list2

print(randomlist(5)) """

""" 
def findletter(word):
    letter = {
        "a" : 0,
        "u" : 0
    }

    letter["a"] = word.count("a")
    letter["u"] = word.count("u")
    return letter
print(findletter("apple is us")) """
        
""" 
def avgruntime():
    runtime = []
    info = {}
    for i in range (0,10):
        runtime.append(float(input("Please enter your best 4 mile run times in sec: ")))
    runtime.sort(reverse=False)
    avg = round(sum(runtime)/len(runtime), 2)
    info["Average"] = f"{int(avg/60)}:{(round(avg%60,2))}"
    info["Best"] = f"{int((runtime[0])/60)}:{(runtime[0]%60)}"
    info["Worse"] = f"{int((runtime[len(runtime)-1])/60)}:{(runtime[len(runtime)-1]%60)}"
    return info

print(avgruntime()) """

""" 
def listmultiplyer(key, number):
    info = {}
    for i in range (0,len(key)):
        info[key[i]] = number[i]
    for i in range (0,len(info)):
        info[f"{key[i]} multi"] = number[i] *5
    return info
start = ["Num 1","Num 2","Num 3"]
number = [5,2,1]
print(listmultiplyer(start,number)) """
""" 
import random
def randomnumbergen(filename):
    number = []
    for i in range (300):
        temp = random.randint(1,2000)
        number.append(temp)
    with open(filename,"w") as f:
        temp = number
        for i in temp:
            f.write(f"{str(i)}\n")
def numberfinder(filename):
    data = []
    output = {}
    testing = ["10",'24','7','11']
    with open (filename,"r") as f:
        data = f.read().splitlines()
    print(data)
    for i in data:
        if i in testing:
            output[i] = data.count(i)
    return output
randomnumbergen("Test.txt")
print(numberfinder("Test.txt")) """

""" 
def combiner(dict1, dict2):
    output = {}
    for key, values in dict1.items():
        output[key] = values
    for key, values in dict2.items():
        if key in output:
            output[key] += values
        else:
            output[key] = values
    return output
test = {"Data":[3], "Info":"NA"}
test2 = {"Data":[5], "Info": "NA"}
print(combiner(test,test2))  """

""" 
import random
def randomnumbergen(filename):
    number = []
    for i in range (300):
        temp = random.randint(1,2000)
        number.append(temp)
    with open(filename,"w") as f:
        temp = number
        for i in temp:
            f.write(f"{str(i)}\n")
def evenorodd(filename):
    data = []
    with open (filename, "r") as f:
        data = f.read().splitlines()
    with open (filename,"w") as f:
        for i in data:
            if int(i) % 2 == 0:
                f.write(f"{i} : Even\n")
            else:
                f.write(f"{i} : Odd\n")
randomnumbergen("Test.txt")
evenorodd("Test.txt") """

""" 
from TestClasses import Dog

brownie = Dog("brown", "brown", 24,24,24)

from TestClasses import Person

burger = Person("Mason", 18, "Snowman")
burger.display()

from TestClasses import Employee

milky = Employee("TY", 15, 16, "DQ special forces")
milky.yearlypay()  """


