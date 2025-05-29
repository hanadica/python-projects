#Hana DiCastri, 1/24
#init
import random
import time
responses = ["It is certain", "Without a Doubt", "Most Likely", "Signs Point to Yes", "You May Rely on it", "Ask Again Later", "Better not tell you now", "Cannot Predict Now", "Concentrate and Ask Again", "Try Again, and your Fate is sealed", "I say no...", "not looking good", "ehhh probably not", "It seems to be No", "Doubtful"]
#func
def magicBall():
    while True:
        x = input("Enter a Yes or No question")
        if x.endswith("?"):
            print("Shaking...")
            time.sleep(2)
            print(random.choice(responses))
            play = input("Would you like to play again? (y)yes or (n)no?")
            if play == "y":
                print("Playing Again!")
            elif play == "n":
                break
            else:
                print("Automatically playing again...")
        else:
            print("please re-enter a question ending with a ?")


#main
magicBall()
