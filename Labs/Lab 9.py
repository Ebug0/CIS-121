
grocerylist = []
costofitem = []
copmliedlist = {}
temp = ""

def samedict(dict1, dict2):
    if dict1 == dict2:
        return("They are the same")
def differencedetector(dict1, dict2):
    purchase1 = []
    purchase1cost = []
    purchase2 = []
    purchase2cost =[]
    for key, values in dict1.items():
        purchase1.append(key)
        purchase1cost.append(values)
    for key,values in dict2.items():
        purchase2.append(key)
        purchase2cost.append(values)
    for i in range (len(purchase1)):
        if purchase1[i] in purchase2:
            for o in range (len(purchase2)):
                if purchase1[i] == purchase2[o]:
                    if purchase1cost[i] > purchase2cost[o]:
                        print(f"{purchase1[i]} is cheaper on purchase 1")
                    elif purchase1cost[i] == purchase2cost[o]:
                        print(f"{purchase1[i]} is the same price on both lists")
                    else:
                        print(f"{purchase2[o]} is cheaper on purchase 2")
                elif purchase2[o] not in purchase1:
                    print(f"{purchase2[o]} is only in purchase 2")
        else:
            print(f"{purchase1[i]} is only in purchase 1") 
 
temp = input("Please enter in a grocery item: ")
while (temp != "DONE"):
    grocerylist.append(temp)
    costofitem.append(int(input("Please enter in the cost of the item: ")))
    temp = input("pleae enter in the grocery item or 'Done' if you are done: ")
for i in range (len(grocerylist)):
    copmliedlist[grocerylist[i]] = costofitem[i]
print(f"My grocery list is {grocerylist}")
print(f"The cost of each item is {costofitem}")
print(copmliedlist)
print(f"The total you have spent of shopping is {sum(costofitem)}") 
seconddict = {
    "Grapes" : 3,
    "Pear" : 7,
    "Orange" : 2
}
finaldict = {
    "Apples": [5, 2],
    "Pear" : [3, 4],
    "Grape" : [10, 3]
}
print(samedict(copmliedlist,seconddict))
differencedetector(copmliedlist, seconddict)
for i in finaldict:
    print(f"Purchase {finaldict[i][0]} {i} at cost of {finaldict[i][1]} each")




