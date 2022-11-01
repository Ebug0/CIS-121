import random 

correctnumber = random.randint(1,100)
winner = False
count = 1
pastguess = 0
print(correctnumber)

while winner == False:
    guess = int(input("Please guess a number: "))
    
    if pastguess == guess:
        print("You guessed that last time try again")
    elif guess > correctnumber:
            print(f"your guess is too large.")
            count += 1
    elif guess < correctnumber:
        print("Your guess is too small")
        count += 1
    elif guess == correctnumber:
        print(f"Congrats! You got the number right in {count} tries!")
        winner = True
    pastguess = guess
    

