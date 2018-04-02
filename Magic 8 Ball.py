#Magic-8 Ball

#Pseudocode:

#Title Card
    #ASCII 8 ball
#Program asks for user question
#One of 20 random responses are generated
    #User's fortune is told.
#Question/answer continued until user quits

#Concepts Used:
    #Triple Quotes
    #Sentry Variable
    #while loops
    #random module
    #if/elif/else operators

#Imports    
import random

print("\n\tAsk the All-Knowing Magic 8 Ball!")
print("""
                   ___________
                  /           \\
                 /   ___       \\
                /   /   \\       \\
                I   \\___/        I
                I   /   \\        I
                I   \\___/        I
                \\               /
                 \\             /
                  \\___________/

 
""")
print("By Rich Williams")
input("\nPress Enter to Begin")
#Question
again = ""
while again != "N":
    input("\n\nWhat is your question? ")

    #Response
    answer = random.randint(1,20)
    if answer == 1:
        print("\nIt is certain")
    elif answer == 2:
        print("\nIt is decidedly so")
    elif answer == 3:
        print("\nWithout a doubt")
    elif answer == 4:
        print("\nYes, definitely")
    elif answer == 5:
        print("\nYou may rely on it")
    elif answer == 6:
        print("\nAs I see it, yes")
    elif answer == 7:
        print("\nMost likely")
    elif answer == 8:
        print("\nOutlook good")
    elif answer == 9:
        print("\nYes")
    elif answer == 10:
        print("\nSigns point to yes")
    elif answer == 11:
        print("\nReply hazy, try again")
    elif answer == 12:
        print("\nAsk again later")
    elif answer == 13:
        print("\nBetter not tell you now")
    elif answer == 14:
        print("\nCannot predict now")
    elif answer == 15:
        print("\nConcentrate and ask again")
    elif answer == 16:
        print("\nDon't count on it")
    elif answer == 17:
        print("\nMy reply is no")
    elif answer == 18:
        print("\nMy sources say no")
    elif answer == 19:
        print("\nOutlook not so good")
    elif answer == 20:
        print("\nVery doubtful")
    else:
        print("error")

    #Exit Option
    again = input("\nAsk another question? Y/N: ")
    again = again.upper()

input("\n\n\nThanks for your questions! Press Enter to Exit")


        
