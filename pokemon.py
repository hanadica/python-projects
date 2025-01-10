#Hana DiCastri
#11/21
#Pokemon Evolution

#inititalize
#global Variables
pokemon_level = 0 #the pokemon starts off at level 0
pokemon_name = "Eevee"#the pokemon is automatically an "Eevee"
day = 1 #the day is day one
import random
save_file = "pokemon_game_save.txt" #this creates a save file for if you want to play again with your past files.
#functions
def save_game(): #this function saves the game
    with open(save_file, "w") as file:
        file.write(pokemon_name + "\n")
        file.write(str(pokemon_level) + "\n")
        file.write(str(day) + "\n")
    print("Game saved successfully!")
def load_game(): #this function loads a saved game
    global pokemon_name, pokemon_level, day
    try:
        with open(save_file, "r") as file:
            pokemon_name = file.readline().strip()
            pokemon_level = int(file.readline().strip())
            day = int(file.readline().strip())
        print("Game loaded successfully!")
    except FileNotFoundError:
        print("No save file found. Start a new game!")
    except ValueError:
        print("Save file is corrupted. Start a new game!")

def drawEevee():#this function draws your pokemon
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫⬜🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫⬜⬜🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫⬜🏿🟧🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧🏿🟧🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧🏿🏿🟧🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧🏿🏿🟧🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧🏿🏿🏿🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🏿🏿🏿🏿🏿🏿🏿🏿
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧🏿🏿🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟫🟧🟧🟧🟧🟧⬜⬜⬜⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧⬛⬛🟧🏿⬜⬜🟫🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟫🟧🟧🟫🏿🏿🏿🏿🟫🟫⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧🏿⬛🏿🟧⬛⬜🟫⬜🏿⬜🟫🏿⬜⬜⬜🟫🟫🟧🟧🟫🏿🏿🏿🏿🏿🟫🟫⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧🏿⬛🟧🏿⬜🏿⬜🟧🏿⬜🏿🏿⬜🏿🟧🟧🟫🏿⬛🏿🏿🏿🏿🟫🟫⬛⬜⬜⬜
⬜⬜⬜🟫🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧🟧🏿🟧🏿🏿⬜🟧🟧🟧🟧🟧🟧🏿🟧🟫🏿⬛⬛⬛⬛🏿🟫🟫⬛⬛⬜⬜⬜⬜
⬜⬜🟫⬜🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟧🟧🏿🟧🟧🟧🟧🟧🟧🟧🟧🟫🟧🟧🟧⬛⬛⬛🏿🟫🟫⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜🟫⬜⬜🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟧🏿🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🏿🏿🟫🟫🟫⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜🟫⬜⬜⬜⬜🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟫🏿⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜🟫⬜⬜⬜⬜⬜🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟧🟧🟧🟧🟧🟧🟧🟧🟧🏿🏿🟧🟫🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟫⬜⬜⬜⬜⬜⬜⬜🏿🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟫🟧🏿🟧🟧🟧🟧🟧🟧🏿⬜🏿🟫🟫🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟫⬜⬜⬜⬜⬜⬜⬜⬜🟫🏿🏿⬜⬜⬜⬜⬜⬜⬜⬜🟫⬛⬜🏿🟧🟫🟧🟧🏿⬛⬛⬛🟫🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟫⬜⬜⬜⬜⬜🟧⬜⬜🟧🟧🟧🏿⬜⬜⬜⬜⬜⬜⬜🟫⬛⬛🟫🟧🟧🟧🟧🟧🏿⬛⬛🟫🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟫⬜⬜🟧⬜⬜🟧🟧⬜🟧🟧🟧🟧🏿⬜⬜⬜⬜🟫🏿🟧⬛⬛🟫🟧🟧🟧🟧🟧🏿⬛🏿🟫🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟫🟧⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🏿⬜⬜🟫⬜🏿🟧🏿⬛🟧🏿🟧🟧🟧🟧🟧🏿🟫🟫🟫🏿⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟫🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🏿⬜🟫⬜🏿🟧🟫🟧🟧🟧🟧🟧🟫🟧🟫🟫🟫🟫🟫🏿⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜🟫🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🏿🟫⬜⬜⬜🏿🟫🟧🟧🟧🏿🏿🟫🟫🟫🟫🟫🟫🏿⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜🏿🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟫🏿⬜⬜⬜🏿🏿🟧🟧🟫🟫🟫🟫🟫🟫🟫🟫🏿⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜🏿🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟫🟫🏿⬜⬜⬜⬜⬜🏿⬛🟫🟫🟫🏿🟫🟫🏿⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜🏿🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟫🟫🟫🏿⬜⬜⬜⬜⬜⬜⬜🏿⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜🏿⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧🟫🟫🟫🟫🏿🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟧🟧🟧🟧🟫🟫🟫🟫🟫🟫🟫🏿🟧🏿⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🏿🟫🟫🟫🟫🟫🟫🟫🟫🏿🟧🟧🏿⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜🟧⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🏿🟫🟫🟫🟫🟫⬛🏿🟧🟧🏿⬜🏿🏿⬜🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜🟧⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜🏿⬛⬛⬛⬛🏿🏿🟧🟧🟧🏿🟧🟧🏿🏿⬜⬜⬜⬜⬜⬜🟧⬜⬜🏿⬜🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟫🟧🟧🟧🟧🟧🟧🟧🟧🏿⬜⬜⬜⬜⬜🟧⬜⬜🏿⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟫🟧🟧🟧🏿⬛🏿🟧🟧🟧🏿🏿⬜⬜🟧⬜⬜🏿🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟫🟫🟧🟧🏿⬜⬛⬛🏿🟧🟧🟧🏿⬜🏿🏿🏿🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟫🟫🟫🟫⬛⬜⬜⬛🏿🏿🟧🟧🟧🟧🏿⬛⬜🏿🟫🟫🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟫🟫🟫🏿🏿⬜⬜⬜🏿🏿🏿🟧🟧🟧⬛⬜⬜🏿🟫🟫🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟫🟫🟫⬛⬜⬜⬜⬜⬛🏿🏿🟧🟧🟧⬛⬜⬜🏿🟫🟧🟧🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟫🏿🏿⬛⬜⬜⬜⬜⬜⬛🏿🟧🟧🟧🟫⬜⬜⬜🏿🟧🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🏿🟧🟫🟧⬛⬜⬜⬜⬜⬜⬜🏿🟫🟧🟫🟫⬛⬜⬜⬛🟫🏿🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜🏿🟫🏿🟫⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def drawEspeon():
    print("""⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬛🟪🟪⬛⬜⬜⬜⬜⬛⬛🟪🟪⬛⬜⬜⬜⬜⬜⬛🟪⬛⬜⬜⬜
⬜⬜⬛🟪🟪🟪⬛⬜⬛⬛🟪🟪🟪⬛⬛⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬜
⬜⬜⬛🟪🟪🟪⬛⬛🟪🟪🟪⬛⬛⬛⬜⬜⬜⬜⬜⬛🟪⬛⬛🟪🟪⬛
⬜⬜⬛🟪🟪⬛🟪🟪🟪🟪⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟪⬛🟪⬛⬛⬜
⬜⬜⬛⬛🟪🟪🟪🟪🟪🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬜⬜⬜
⬜⬛🟪⬛⬜🟥🟪🟪🟪⬛🟪⬛⬜⬛⬛⬛⬛⬛⬜⬜⬛🟪⬛⬜⬜⬜
⬛🟪⬛⬛🟥🟥🟪🟪⬜⬛🟪🟪⬛🟪🟪🟪⬛🟪⬛⬛⬛🟪⬛⬜⬜⬜
⬜⬛⬛⬛🟪🟪🟪⬜🟪⬛🟪🟪🟪⬛🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜
⬜⬜⬜⬛🟪🟪🟪⬛⬛🟪⬛⬛🟪🟪⬛🟪🟪⬛⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟪🟪🟪🟪⬛🟪🟪⬛⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪⬛🟪⬛🟪⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪⬛🟪🟪⬛🟪⬛⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛🟪🟪⬛⬛⬜⬜⬛🟪⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟪🟪⬛⬜⬜⬛🟪⬛⬜⬜⬜⬛🟪⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛🟪⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def drawSylveon():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⡤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠞⠀⢀⣳⠔⠊⢉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡎⢀⠔⠋⠀⠀⣠⣎⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡸⢸⠾⣅⡀⠐⡄⠈⠁⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠗⠓⠢⡄⠙⡆⠘⢀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡠⠋⠀⠀⠀⢸⣀⡷⠚⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠋⠁⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡰⠁⠀⠀⠀⣠⡞⢹⡆⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠉⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡇⠀⠀⣠⠊⠀⡇⠸⡇⠀⢀⡇⠀⠀⣀⠀⠀⠀⢠⠞⠁⠀⣀⡀⠀⠀⠀⢀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⡇⠀⢰⢻⠀⠀⡇⢰⡇⠀⣸⠀⣰⠋⠈⢳⡀⡴⠃⢀⡴⠊⢡⠃⠀⠀⡰⢫⠏⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠒⠉⣩⠇⠀
⠀⠈⠦⣝⠘⡆⠀⢇⢸⠁⢠⠟⢶⠃⠀⠀⡀⢿⠁⡰⠋⠀⡰⠃⠀⠀⢋⡴⠃⠀⠀⠀⠀⠀⢀⣴⠚⠯⡀⠀⠀⠈⢉⣩⠇
⠀⠀⠀⢿⡛⠻⣄⡘⡏⠀⣾⣀⡎⠀⠀⡸⠀⠘⡼⠁⣠⣾⠥⠤⠤⢶⡋⠀⠀⠀⠀⠀⡠⠞⠁⠈⠙⡆⢹⣠⠴⠊⠉⠀⠀
⠀⠀⠀⢠⡵⢤⠀⠙⠂⠈⠁⠀⢇⠀⠀⢇⠀⠀⠛⠉⠁⣸⠀⠀⠀⢸⠃⠀⠀⢀⡤⠊⠀⠀⠀⠀⢀⡿⠚⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢩⣯⠖⢋⠑⠲⣄⠀⠘⠦⠤⠼⠚⣿⣀⣠⠔⠁⠀⠀⣠⠏⢀⣠⠔⠋⠀⠀⠀⠀⣠⠖⠻⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡞⢁⠞⢩⠙⡆⠘⡆⢀⡴⠊⣉⠙⢾⣀⣀⣀⡠⠴⠞⠓⠒⠉⠀⠀⠀⠀⢀⡤⠞⢹⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⠃⢸⠀⠸⢤⡇⠀⣱⠋⣰⠛⡏⢣⠘⡆⠈⠓⠦⢄⣀⣀⣀⣀⣀⡠⠴⠚⠁⠀⠀⡜⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⡄⠈⠓⠒⠊⠀⠠⠤⠀⢧⠒⠁⡼⢠⠃⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣦⠤⣄⠀⠳⢤⡠⠴⢪⡑⠋⢀⡼⠀⢀⡠⠒⠉⠀⠀⢀⣉⡲⣄⠀⠀⠀⡴⠃⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⡌⠳⣵⠋⣇⠀⢠⡷⠚⠉⢀⠔⠋⠀⠀⣠⠔⠫⣅⠀⠈⠈⢳⣤⠞⠁⢀⣀⡤⣾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢧⠀⢱⡀⡁⢀⡇⠀⡼⣙⡦⠞⠁⠀⠀⢠⣞⣁⡤⠤⢬⣳⣠⠴⠊⠀⠀⠒⠉⣠⠔⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡼⠣⣀⡽⠛⢯⣀⠾⣉⡁⠀⠀⣀⡠⠞⠁⠀⠀⠀⠀⠀⠀⠉⠢⡤⠤⢶⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡞⠀⢠⢿⠀⠀⠁⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⣰⠂⠀⠀⠀⠘⢆⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡼⠀⠀⡞⢸⠀⠀⠀⠀⢠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠘⣆⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣇⠀⠀⣷⡘⡆⠱⣄⠀⡞⠀⠀⠀⠀⢀⠀⡀⠀⠀⣀⣘⠀⠀⠀⠀⠀⠀⠀⠸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣄⠀⢹⡉⠻⡄⠈⢲⠁⠀⠀⠀⢀⣎⡤⠤⠔⢶⠤⠌⣧⡀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠓⠤⣑⡄⠱⡄⡏⠀⠀⠀⣠⠏⠁⠀⠀⠀⠈⠣⡀⠀⠈⠓⣤⣀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣻⠁⠀⢀⡜⢹⡄⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⢸⡈⠑⡆⠀⠀⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⠇⠀⢠⠎⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⢀⡇⢀⣼⠁⢀⡇⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠣⣀⠀⡾⣄⢴⠯⢤⡴⡇⠀⠀⠀⠀⠀⠀⠀⠀⡼⠛⢱⠇⠀⢸⠷⢋⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⣞⣉⣁⡼⠁⢡⣿⣶⠋⢰⡇⠀⠀⠀⠀⠀⠀⢀⡴⠃⢠⠏⠀⣰⠇⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⢋⡀⢀⡞⢸⣳⣠⠞⠀⠀⠀⠀⠀⠀⠀⠸⠼⠵⠋⠀⣾⢇⣆⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⠯⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
def train(): #this function makes your pokemon level up once
    print(pokemon_name + " did 10 push ups!, " + pokemon_name + " leveled up!")
    global pokemon_level
    pokemon_level = pokemon_level + 1
def gymBattle(): #This function is a chance of winning or losing, which will either make ur pokemon gain levels or stay the same
    winorlose = int(input(pokemon_name + " is battling a wild pokemon! Will " + pokemon_name + " win? pick a number, 1 or 2?"))
    global pokemon_level
    if winorlose == random.randint(1,2):
        pokemon_level = pokemon_level + 2
        print(pokemon_name + " won the battle! " + pokemon_name + " gained 2 levels!")
    else:
        print(pokemon_name + " lost the battle...")
def rest():#this function shows your pokemons level
    global pokemon_level
    print(pokemon_name + " is level " + str(pokemon_level) + "!")
    if pokemon_level < 5 :
        drawEevee()
    elif pokemon_level > 5 and pokemon_level < 10 :
        drawEspeon()
    else:
        drawSylveon()

def evolution(): #this function will evolve your pokemon once it gets to a certain level
    global pokemon_level
    global pokemon_name
    if pokemon_level == 5 and pokemon_name != "espeon" :
        print("Your " + pokemon_name + " is evolving!")
        pokemon_name = "Espeon"
        print("Your Eevee evolved into " + pokemon_name)
        drawEspeon()
    elif pokemon_level == 10 and pokemon_name != "sylveon":
        print("Your " + pokemon_name + " is evolving!")
        pokemon_name = "Sylveon"
        print("Your Espeon evolved into " + pokemon_name)
        drawSylveon()

#main
print("Welcome to Pokemon Evolution!")
gamefile = input("Do you want to start a new game(1) or reload a previous game(2)?")
if gamefile == "2":
    load_game()
    while True :
        print("Welcome to Pokemon Evolution!")
        print("Choose an activity for Day: " + str(day))
        activity = input("""1. Train
            2. Gym Battle
            3. Rest(Display Info)
            4. Quit
            5. Save Game""")
        if activity == "1":
            train()
            evolution()
            day = day + 1 #this function adds a day to the cycle
        elif activity == "2":
            gymBattle()
            evolution()
            day = day + 1
        elif activity == "3":
            rest()
            day = day + 1
        elif activity == "4":
            print("Thanks for playing!")
            break
        elif activity == "5":
            save_game()
        else:
            print("Thats not an option! type only the number of what activity you would like to do!")
        if day >= 50 :
            final = input("You have the option to fight the Boss level, do you accept or decline this challenge?")
            #this is a final boss battle you can do after you reach day 50
            if final == "accept" :
                if pokemon_level <= 50 :
                    bossbattle = input("An evil pokemon trainer showed up with their level 50 pokemon!, pick a number between 1 and 5")
                    if bossbattle == random.randint(1,5):
                        print("You beat the evil pokemon trainer!! congrats you are now the pokemon champion!")
                    else:
                        print("your pokemon fled the battle after your opponents pokemon attacked...")
                elif pokemon_level > 50 :
                    bossbattle50 = input("An evil pokemon trainer showed up with their level 50 pokemon!, pick a number between 1 and 2")
                    if bossbattle50 == random.randint(1,2):
                        print("You beat the evil pokemon trainer!! congrats you are now the pokemon champion!")
                    else:
                        print("your pokemon fled the battle after your opponents pokemon attacked...")
            elif final == "decline" :
                print(pokemon_name + " stayed in today...")
            else :
                print("That not an option!")
elif gamefile == "1" : #this is if you didn't have a previous save file.
    while True :
        print("Welcome to Pokemon Evolution!")
        print("Choose an activity for Day: " + str(day))
        activity = input("""1. Train
            2. Gym Battle
            3. Rest(Display Info)
            4. Quit
            5. Save Game""")
        if activity == "1":
            train()
            evolution()
            day = day + 1
        elif activity == "2":
            gymBattle()
            evolution()
            day = day + 1
        elif activity == "3":
            rest()
            day = day + 1
        elif activity == "4":
            print("Thanks for playing!")
            break
        elif activity == "5":
            save_game()
        else:
            print("Thats not an option! type only the number of what activity you would like to do!")
        if day >= 50 :
            final = input("You have the option to fight the Boss level, do you accept or decline this challenge?")
            if final == "accept" :
                if pokemon_level <= 50 :
                    bossbattle = input("An evil pokemon trainer showed up with their level 50 pokemon!, pick a number between 1 and 5")
                    if bossbattle == random.randint(1,5):
                        print("You beat the evil pokemon trainer!! congrats you are now the pokemon champion!")
                    else:
                        print("your pokemon fled the battle after your opponents pokemon attacked...")
                elif pokemon_level > 50 :
                    bossbattle50 = input("An evil pokemon trainer showed up with their level 50 pokemon!, pick a number between 1 and 2")
                    if bossbattle50 == random.randint(1,2):
                        print("You beat the evil pokemon trainer!! congrats you are now the pokemon champion!")
                    else:
                        print("your pokemon fled the battle after your opponents pokemon attacked...")
            elif final == "decline" :
                print(pokemon_name + " stayed in today...")
            else :
                print("That not an option!")
