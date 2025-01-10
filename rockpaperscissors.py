#Hana DiCastri
#1/6/2025
#Rock Paper Scissors
#init
import random
cscore = 0 #this is the computers score before starting
pscore = 0 #this is the players score before starting
ties = 0 #this is how many ties there are before starting
#func
def rpsgame():
    while True:
        print("Welcome to Rock Paper Scissors!")
        rps = random.randint(1,3)#this picks a number between 1 and 3, with each number meaning a different play
        #1 = rock, 2 = paper, 3 = scissors
        playerps = input("Rock Paper or Scissors?")#the player inputs if they play rock paper or scissors
        if rps == 1 and playerps == "rock":
            print("You both played rock")
            global ties#globalizing variables allows for the variables to be used inside functions
            ties = ties + 1
        elif rps == 1 and playerps == "paper":
            print("Computer shows rock, You won!")
            global pscore
            pscore = pscore + 1
        elif rps == 1 and playerps == "scissors":
            print("Computer shows rock, You lost...")
            global cscore
            cscore = cscore + 1
        elif rps == 2 and playerps == "rock":
            print("Computer shows paper, You lost...")
            cscore = cscore + 1
        elif rps == 2 and playerps == "paper":
            print("You both played paper.")
            ties = ties + 1
        elif rps == 2 and playerps == "scissors":
            print("Computer shows paper, You won!")
            pscore = pscore + 1
        elif rps == 3 and playerps == "rock":
            print("Computer shows scissors, You won!")
            pscore = pscore + 1
        elif rps == 3 and playerps == "paper":
            print("Computer shows scissors, You lost...")
            cscore = cscore + 1
        elif rps == 3 and playerps == "scissors":
            print("You both played scissors.")
            ties = ties + 1
        else:
            print("That isn't an option!")#this is shown when the user puts in something other than "rock", "paper", or "scissors"
        print("Your score is " + str(pscore) + ", and the computer's score is " + str(cscore) + ". You tied " + str(ties) + " time(s).")
        wyl = input("Would you like to continue playing?")#at the end, it shows you your score, as well as the computers score, and ties
        if wyl == "no" or wyl == "No": #wyl stands for would you like, and if they dont want to play, the function will end.
            print("Thank you for playing!")
            break
        elif wyl != "yes" or wyl != "Yes":
            print("That isn't an option, continuing the game...")
#main
rpsgame()
