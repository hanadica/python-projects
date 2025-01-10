#Hana DiCastri Number Guesser 11/11/2024
#init

import random
#func

def numberGuessdif (): #this function allows for users to play the number guessing game
    difficulty = input("pick a difficulty - easy, medium, or hard")#the user can pick a difficulty
    if difficulty == "easy":
        guess = input("Enter a number 1-5")#here is where the user guesses the number
        randomnumber = random.randint(1,5)#this randomly picks a number between 1 and 5
        if guess == randomnumber :
            print(guess + " is the correct number")#the function shows the user what the code's random number was
        else:
            print(guess + " is the wrong number, the correct number is " + str(randomnumber) )
    elif difficulty == "medium":
        mguess = input("Enter a number 1-10") #i used the variable "mguess" for medium guess, as to not confuse the code with repeating the variable "guess"
        mrandomnumber = random.randint(1,10)
        if mguess == mrandomnumber :
            print(mguess + " is the correct number")
        else:
            print(mguess + " is the wrong number, the correct number is " + str(mrandomnumber))
    elif difficulty == "hard":
        hguess = input("Enter a number 1-20")
        hrandomnumber = random.randint(1,20)
        if hguess == hrandomnumber :
            print(hguess + " is the correct number")
        else:
            print(hguess + " is the wrong number, the correct number is " + str(hrandomnumber) )
    else:
        print("That is not a difficulty, try again") #this prints if any other option is provided for the question


#main
numberGuessdif()
