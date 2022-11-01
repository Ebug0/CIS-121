

def minium(data):
    if len(data) == 0:
        return("Empty list can not be used")
    if len(data) == 1:
        return data
    else:
        if data[0] <= data[1]: # if the first value is less then the second value get rid of seconds value
            data.pop(1)
        elif data[0] >= data[1]: # if the second value is less then the second value get rid of the first value
            data.pop(0)
        minium(data)
    return data
def maxium(data):
    if len(data) == 1:
        return data
    else:
        if data[0] >= data[1]:# if the first value is greater then the second value get rid of seconds value
            data.pop(1)
        elif data[0] <= data[1]: # if the second value is less then the second value get rid of the first value
            data.pop(0)
        maxium(data)
    return(data)
def Extrema(data, min=True,max=True):
    temp = []
    for i in data:
        temp.append(i)
    if min == True:
        minium(data)
    if max == True:
        maxium(temp)
    if min == False and max == False:
        return("Nothing was done")
    if max == False:
        return data
    elif min == False:
        return temp
    else:
        return data, temp

maxlist = []
orglist = []
numlist = []
with open ("randomValues.txt","r") as f: #Gets data from file
    orglist = f.read().splitlines()
for i in orglist: # gets only the  numbers
    if i.isdigit() == True:
        numlist.append(int(i))
for i in numlist:
    maxlist.append(i) #
extralist = numlist.copy()
print(minium(numlist))
print(maxium(maxlist))
print(Extrema(extralist))
