from os import truncate


userinput = True
number = 0
userlist = []
import statistics

while userinput == True:
    number = input("Please enter in a number to a list or enter done: ")
    if number == "done":
        userinput = False
    else:
        userlist.append(int(number))
userlist.sort()

print(f"Sum {sum(userlist)}, Mean {statistics.mean(userlist)}, Median {statistics.median(userlist)}, Greatest {userlist[len(userlist)-1]}, Smallest {userlist[0]}")


