#slot machine
#hana dicastri
#init
import random
import time
slot_symbols = ["7","♥","♦","♠","♣","♥","♦","♠","♣"]
credits = 100
#functions
#1. ask player if they'd like to spin or quit
print("Welcome to the Slot Machine!")
print("Slot Machine Symbols : " + str(slot_symbols))
print("You have 100 credits.")
print("Press S to spin and Q to Quit")
while True:
    quitornot = input("Spin the slots? (S) or (Q)")
    if quitornot == "S" and credits > 0:
        bet = int(input("How many credits do you want to bet?"))
        credits = credits - bet
        print("minus " + str(bet) + " credits")
        print("Spinning...")
        time.sleep(1)
        x = random.choice(slot_symbols)
        print(x + " _ _")
        y = random.choice(slot_symbols)
        time.sleep(1)
        print(x + " " + y + " _ ")
        z = random.choice(slot_symbols)
        time.sleep(1)
        print(x + " " + y + " " + z)
        if x!= "7" and x == y and y == z :
            print("Win!")
            betamount = bet*10
            credits = credits + betamount
            print("You gained " + str(credits) + " credits! you now have " + str(credits) + " credits!")
        elif x == "7" and x == y and y == z:
            print("Jackpot!")
            betamount = bet*50
            credits = credits + betamount
            print("You gained " + str(credits) + " credits! you now have " + str(credits) + " credits!")
        elif x == y or y == z or x == z:
            print("Two of a Kind!")
            betamount = bet*5
            credits = credits + betamount
            print("You gained " + str(credits) + " credits! you now have " + str(credits) + " credits!")
        else:
            print("loss...")
            print("You now have " + str(credits) + " credits.")
    elif quitornot == "Q":
        print("Thank you for playing! you ended with " + str(credits) + " credits!")
        break
    elif credits == 0:
        print("Out of Credits! Try again later.")
    else:
        print("Not an option...")

