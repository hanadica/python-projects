#Hana DiCastri, 12/10/2024

nadj = input("Please enter a negative adjective.")#this takes the users negative adjective and puts it into a variable, which allows the code to print it when it runs the "nadj"
animal = input("Please enter an animal")
place = input("please enter a place")
padj = input("please enter a positive adjective.")
oanimal = input("please enter a second animal")
#all the variables above are entered by the user and are then put into the story below, which allows users to create a unique story based on their inputs
print("""
      Once upon a time, there was a """ + str(nadj) + """ """ + str(animal) + """. It went around """ + str(place) +
      """ and was rejected by all the other """ + str(animal) + """'s. One day, the """ + str(nadj) + """ """ + str(animal) +
      """ ran into a group of """ + str(oanimal) + """'s. They told the """ + str(animal) + """ that it actually isnt a """ +
      str(nadj) + """ """ + str(animal) + """, and was in fact a """ + str(padj) + """ """ + str(oanimal) + """! The End.""")

