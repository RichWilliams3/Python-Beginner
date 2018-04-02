#Evens-Odds Game

#Pseudocode:

#Player guesses whether total will be even or odd, computer takes other option
#Player decides how many fingers they will throw between 0 and 5
#Computer generates a random number between 0 and 5
#The total is calculated
#Whoever has the correct pick wins
#Wins are tallied
#Player chooses how many times to keep playing
#When Player exits, total Win/Loss is shown before program ends.

#Concepts Used:
    #while loops
        #sentry variables
    #and operator
    #or operator
    #random module
    #str()
    #int()
    #Concatenating Strings
    #Augmented Operators

#Imports
import random

print("\nEvens or Odds")
print("\n\n\nBy Rich Williams")
input("\nPress Enter to Begin")

user_score = 0
comp_score = 0
stay = ""
while stay != "N":
    pick = ""
    while pick != "E" and pick != "O":
        pick = input("\nPick \'E\' for Evens or \'O\' for Odds: ")
        pick = pick.upper()
    user = 6
    while user > 5 or user < 0:
        user = int(input("How many fingers will you throw? (0-5) "))
    computer = random.randrange(6)
    total = user + computer
    if pick == "E":
        if total == 0 or total == 2 or total == 4 or total == 6 or total == 8 or total == 10:
            print("Computer throws: " + str(computer))
            print("\nTotal fingers: " + str(total))
            print("It's Evens! You win!")
            user_score += 1
            print("\nUser: " + str(user_score) + "\tComputer: " +
                  str(comp_score))
        else:
            print("Computer throws: " + str(computer))
            print("\nTotal fingers: " + str(total))
            print("It's Odds. You lose...")
            comp_score += 1
            print("\nUser: " + str(user_score) + "\tComputer: " +
                  str(comp_score))
    else:
        if total == 1 or total == 3 or total == 5 or total == 7 or total == 9:
            print("Computer throws: " + str(computer))
            print("\nTotal fingers: " + str(total))
            print("It's Odds! You win!")           
            user_score += 1
            print("\nUser: " + str(user_score) + "\tComputer: " +
                  str(comp_score))
        else:
            print("Computer throws: " + str(computer))
            print("\nTotal fingers: " + str(total))
            print("It's Evens. You lose...")
            comp_score += 1
            print("\nUser: " + str(user_score) + "\tComputer: " +
                  str(comp_score))

    stay = input("\nPlay again? (Y/N) ")
    stay = stay.upper()

print("\nFinal Score:")
print("\nUser: " + str(user_score) + "\tComputer: " +
      str(comp_score))
input("\n\nThanks for Playing! Press Enter to Exit")
