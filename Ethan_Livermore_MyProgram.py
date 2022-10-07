import Ethan_Livemore_Stats2
#this file is for the group Ethan Livermore and Mason Snow
file = open("50DayFruitData.txt","r")
data = file.read().splitlines()
data.pop(0)
apples = []
file.close()

for i in data:
    temp = i.split() #makes each line its own list to call in the if statements below
    
    if temp[1] == "apple":
        apples.append(int(temp[2])) #adding value to the apple list

with open("Ethan_Livermore_Output.txt", "w") as f:
    f.write(f"The mean number of apples eat is {round(Ethan_Livemore_Stats2.takemean(apples),2)}\nThe median number of apples eat is {Ethan_Livemore_Stats2.takemedian(apples)}\n\
The mode number of apples is (are) {Ethan_Livemore_Stats2.takemode(apples)}")#takes the median, mode, and mean of the apple list and writes it to the file
