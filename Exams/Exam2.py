#Start of problem 1
def evenorodd(data, outfile):
    result =  {             # makes the result dict
        "Even" : "",
        "Odd" : ""
    }
    for i in data:
        if int(i) % 2 == 0:
            result["Even"] += f"{str(i)} "
        else:                               #adds the even or odd datas to the dict 
            result["Odd"] += f'{str(i)} '
    with open (outfile, "w") as f:
        for i in result:            #writes the dict to the file that is given to the function
            f.write(f"{i} : {result[i]}\n")
test = [5,3,2,1,6,7,12,543,12,3,43,58]
evenorodd(test, "Test.txt")

#start of problem 2
import random

list1 = []
list2 = []
numbers = {}        #declares lists and dict for global use
for i in range (200):
    list1.append(random.randint(1,100))
    list2.append(random.randint(1,100))     #makes two list with 200 random numbers ranging from 1,100
combinedlist = list1+list2 #combines the list for calculcations
for i in combinedlist:
    if combinedlist.count(i) > 1:    #adds the duplicated numbers to a dictionary and how many there are
        numbers[i] = combinedlist.count(i)
with open("RESULTS4.txt", "w") as f:
    for key, values in numbers.items(): #writes the dictionary to the file
        f.write(f"{key} : {values}\n")
print(numbers)      #displays duplicated values

#Start of Problem 3
import statistics
data = []
result = {}
newdata = [] #decalres lists and dict for global use
with open ("steps.txt", "r") as f:  #gets data from the file
    data = f.read().splitlines()
for i in data:
    newdata.append(int(i))      #turns the data from a str to an int
result["Month"] = "Average"
result["January"] = round(statistics.mean(newdata[0:31]),1)
result["February"] = round(statistics.mean(newdata[31:59]),1)
result["March"] = round(statistics.mean(newdata[59:90]),1)
result["April"] = round(statistics.mean(newdata[90:120]),1)
result["May"] = round(statistics.mean(newdata[120:151]),1)
result["June"] = round(statistics.mean(newdata[151:181]),1)
result["July"] = round(statistics.mean(newdata[181:212]),1)
result["August"] = round(statistics.mean(newdata[212:243]),1)
result["September"] = round(statistics.mean(newdata[243:273]),1)
result["October"] = round(statistics.mean(newdata[273:304]),1)
result["November"] = round(statistics.mean(newdata[304:334]),1)
result["December"] = round(statistics.mean(newdata[334:365]),1)         #calculates the mean for each month and adds it to the dict
print(result)   #prints dict
with open ("steps_by_month.txt", "w") as f:
    for key, value in result.items():
        f.write(f"{key} : {value}\n") #writes dict to the file

#Start of bonus questions

from asyncio.windows_events import NULL


def findnumber(list, numbertofind):
    if len(list) == 0:
        print("That number was not in this list")
    elif str(list[0]) != str(numbertofind):
        list.pop(0) #if numbertofind is not in the first index get rid of the first index then call the functino again without that index
        findnumber(list,numbertofind)
    elif str(list[0]) == str(numbertofind) and len(list) != 0:  #if the first index is equal to the numbertofind print that number was in the list
        print("That number was in the list") 
list = [1,2,3,4,5,6,8,9,19]
findnumber(list, 9)