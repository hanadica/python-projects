#HANA DICASTRI 1/8/2025
#init
import random
wscore = 0 #this is the amount of wins before you start
lscore = 0 #this is the amount of loses before you start
#func
def Ask_question():
    print("Welcome to the Multiplication Game!")
    difficulty = input("Would you like your quiz to be easy, medium, hard, or endless?")
    if difficulty == "endless":
        while True:#the while true allows for the function to keep running until the "break"
            edifficulty = input("You are now in endless mode.. would you like an easy, medium, hard question or would you like to quit?")
            if edifficulty == "easy":
                x = random.randint(1, 5)#easy mode picks two numbers between 1 and 5 to multiply
                y = random.randint(1, 5)
                global lscore
                global wscore
                solution = input("What is " + str(x) + " multiplied by " + str(y) + "?")
                if solution == str(x * y):
                    print("congrats! the answer is " + str(x * y))
                    wscore = wscore + 1 #when you win, your win score increases by 1
                    print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + "time(s).")
                else:
                    print("you were wrong... the answer was " + str(x * y))
                    lscore = lscore + 1
                    print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + " time(s).")
            elif edifficulty == "medium": #does ths same as easy, just picks between 1 and 10 rather than 1 and 5
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                solution = input("What is " + str(x) + " multiplied by " + str(y) + "?")
                if solution == str(x * y):
                    print("congrats! the answer is " + str(x * y))
                    wscore = wscore + 1
                    print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + "time(s).")
                else:
                    print("you were wrong... the answer was " + str(x * y))
                    lscore = lscore + 1
                    print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + " time(s).")
            elif edifficulty == "hard":
                x = random.randint(1, 20)
                y = random.randint(1, 20)
                solution = input("What is " + str(x) + " multiplied by " + str(y) + "?")
                if solution == str(x * y):
                    print("congrats! the answer is " + str(x * y))
                    wscore = wscore + 1
                    print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + "time(s).")
                else:
                    print("you were wrong... the answer was " + str(x * y))
                    lscore = lscore + 1
                    print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + " time(s).")
            elif edifficulty == "quit":
                break#this ends the infinite loop
            else:
                print("Thats not an option!")
    elif difficulty == "easy": #everything below is repeated, just without endless mode
        questions = input("How many questions would you like to answer on this quiz?") #in non-endless mode, you can pick how many questions you want to answer
        for i in range(int(questions)):
            x = random.randint(1, 5)
            y = random.randint(1, 5)
            solution = input("What is " + str(x) + " multiplied by " + str(y) + "?")
            if solution == str(x * y):
                print("congrats! the answer is " + str(x * y))
                wscore = wscore + 1
                print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + "time(s).")
            else:
                print("you were wrong... the answer was " + str(x * y))
                lscore = lscore + 1
                print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + " time(s).")
    elif difficulty == "medium":
        questions = input("How many questions would you like to answer on this quiz?")
        for i in range(int(questions)):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            solution = input("What is " + str(x) + " multiplied by " + str(y) + "?")
            if solution == str(x * y):
                print("congrats! the answer is " + str(x * y))
                wscore = wscore + 1
                print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + "time(s).")
            else:
                print("you were wrong... the answer was " + str(x * y))
                lscore = lscore + 1
                print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + " time(s).")
    elif difficulty == "hard":
        questions = input("How many questions would you like to answer on this quiz?")
        for i in range(int(questions)):
            x = random.randint(1, 20)
            y = random.randint(1, 20)
            solution = input("What is " + str(x) + " multiplied by " + str(y) + "?")
            if solution == str(x * y):
                print("congrats! the answer is " + str(x * y))
                wscore = wscore + 1
                print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + "time(s).")
            else:
                print("you were wrong... the answer was " + str(x * y))
                lscore = lscore + 1
                print("your were correct " + str(wscore) + " time(s), and you were incorrect " + str(lscore) + " time(s).")
    else:
        print("That isn't an option...")
    print("congrats you finished! you were correct " + str(wscore) + " times, and you were incorrect " + str(lscore) + " times.")#this shows the score after any mode and however many questions
#main
Ask_question()
