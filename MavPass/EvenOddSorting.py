from asyncio.windows_events import NULL
import random

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")

def DicCreater():
    even = []
    odd = []
    number = []
    temp = {}
    run = 0
    oddlarger = False
    for i in range(200):
        ran = random.randint(0,100)
        number.append(ran)
    for i in range (200):
        if number[i] %2 == 0:
            even.append(number[i])
        else:
            odd.append(number[i])
    if len(odd)<len(even):
        odd.extend(['X'] * (len(even)-len(odd)))
    else:
        even.extend(['X'] * (len(odd)-len(even)))
    for i in odd:
        if i in temp:
            odd.pop(i)
        else:
            temp[i] = 0
    print(temp)
    if len(even) == len(odd):
        print("TRUE")
    if len(odd) == len(list(temp)):
        print("dumbass")
    print(len(list(temp)))
    print(len(odd))

    for i in range (0,len(odd)):
        keys = list(temp)
        temp[keys[i]] = even[i]
    return temp

    


print(DicCreater())