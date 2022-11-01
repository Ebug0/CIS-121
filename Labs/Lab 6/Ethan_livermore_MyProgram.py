import Ethan_Livermore_Stats

path = "C:\\Users\\ethan\\Desktop\\CIS  121\\Labs\\Lab 6\\500DayFruitData.txt"
file = open(path , "r") #opening file in read mode

data = file.read().splitlines()
data.pop(0) #getting rid of header
apples = []
strawberry = []
banna = []
#Declaring lists for use in for statement

for i in data:
    temp = i.split() #makes each line its own list to call in the if statements below
    
    if temp[1] == "apple":
        apples.append(int(temp[2]))
    elif temp[1] == "strawberry":
        strawberry.append(int(temp[2]))
    elif temp[1] == "banana":
        banna.append(int(temp[2]))
    #adding the vaules to the fruit lists

mean = f"Mean: Apples {Ethan_Livermore_Stats.meanE(apples)}    Strawberry {Ethan_Livermore_Stats.meanE(strawberry)}    Bananna {Ethan_Livermore_Stats.meanE(banna)}\n"
median = f"Median: Apples {Ethan_Livermore_Stats.median(apples)}    Strawberry {Ethan_Livermore_Stats.median(strawberry)}    Bananna {Ethan_Livermore_Stats.median(banna)}" 
#getting the mean and median for the fruits

with open ("C:\\Users\\ethan\\Desktop\\CIS  121\\Labs\\Lab 6\\Ethan_Livermore_OutputText.txt", 'w') as o:  #writing to the output txt file
    o.write(mean)
    o.write(median)
