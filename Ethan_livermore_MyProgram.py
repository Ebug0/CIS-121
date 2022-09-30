import Ethan_Livermore_Stats

path = "C:\\Users\\ethan\\Desktop\\CIS  121\\Labs\\Lab 6\\500DayFruitData.txt"
file = open(path , "r") #opening file in read mode

data = file.read().splitlines()
data.pop(0)
apples = []
strawberry = []
banna = []


for i in data:
    temp = i.split()
    
    if temp[1] == "apple":
        apples.append(int(temp[2]))
    elif temp[1] == "strawberry":
        strawberry.append(int(temp[2]))
    elif temp[1] == "banana":
        banna.append(int(temp[2]))

mean = f"Mean: Apples {Ethan_Livermore_Stats.meanE(apples)}    Strawberry {Ethan_Livermore_Stats.meanE(strawberry)}    Bananna {Ethan_Livermore_Stats.meanE(banna)}\n"
median = f"Median: Apples {Ethan_Livermore_Stats.median(apples)}    Strawberry {Ethan_Livermore_Stats.median(strawberry)}    Bananna {Ethan_Livermore_Stats.median(banna)}"

with open ("C:\\Users\\ethan\\Desktop\\CIS  121\\Labs\\Lab 6\\Ethan_Livermore_OutputText.txt", 'w') as o: 
    o.write(mean)
    o.write(median)
print("done")