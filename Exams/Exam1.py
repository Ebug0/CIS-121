#Ethan Livermore
#1.A code does not run. You will need to make the Age input be casted as an int instead of a string
#1.B Code runes an inf loop. to fix this you will need to increment the variable by x amount each time 
#1.C Code runes fine
#1.D Code does not run. You will need to indent the print statement to make sure its in the for loop
#1.E Code does not run. you will either need to cast the input as an int instead of a string or make the 5 in the condiational a string by adding quotes

#start of problem 2
milk = int(input("Please enter how much milk you would like to get: "))
eggs = int(input("Please enter how much many eggs you would like: "))
bacon = int(input("Please enter how much backon you would like to get: "))
sum2 = ((milk*2)+(eggs*1.5)+(bacon*3)) #adding the dollar amount of each item together
taxsum = sum2 *1.11 #finds the final cost of the items with tax
print(f"You got {milk} milk, {eggs} eggs, and {bacon} bacon. Your total cost before tax is ${sum2}, and total cost after tax ${taxsum}")

#start of problem 3
phone = ("7875551212") #sets phone variable equal to the 10 digit number provided
print(f"your readable phone number is: ({phone[0:3]}) {phone[3:6]}-{phone[6:10]}") #prints out readable phonenumber with a formatted string

#start of problem 4
import random
randomnum =0
divisor = 0
while (divisor < 10): #runs loop till 10 divisors are found
    randomnum = random.randrange(1,60) #gets a random number 1 - 60
    
    if(48%randomnum == 0): #see if the random number is a divisor of 48 and if yes then increment "divisor" variable by 1
        divisor +=1
    if(randomnum%2 == 0): #checks to see if random number is even
        print(f"Even {randomnum}")
    if randomnum >= 15: #checks to see if random number is greater or equal to 15
        print(f"”I generated the number {randomnum}, randomly")