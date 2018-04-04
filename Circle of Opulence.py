#Circle of Opulence

#Pseudocode:

#6 Rounds, with a chance at a bonus 7th Round
#User Given a random Puzzle out of these categories:
    #Former & Latter
    #Verse Purse
    #Individuals
    #Locations
    #Objects
    #Notions
    #Party On!
#User given puzzle, with letters as underscores
#Two Options:
    #1. Rotate the Circle of Opulence
    #2. Solve the Puzzle
#1. Rotate Circle Options (randomly generated):
    #Cash
        #16/24 odds
        #User guesses a letter
        #If letter in puzzle, gets cash
            #Cash multiplied by number of letters
    #POVERTY
        #If POVERTY, cash and prizes deleted for puzzle
            #If user in defecit for the round, debt doubled
    #PRIZE
        #Prize with cash amount
        #Cash amount added to winnings
        #Prizes unique
            #Can't win duplicates
            #If a single prize is lost, it can't be recovered
    #SAVE
        #Gives user chance to save winnings if POVERTY is spun
    #Once the circle result is given, user guesses letter
        #If the letter is in the puzzle
            #Cash times the letter count is added
            #Prize is added to the prize bank
            #A save is added
        #If the letter isn't in the puzzle or was already guessed
            #Cash is subtracted from the winnings
            #The prize amount is subtracted from the winnings
            #If save is failed, half winnings lost
#2. Solve the Puzzle
    #User asked to solve puzzle
        #If the answer matches the statement, round over
        #Otherwise the round continues
    #If all letters filled, user can still spin
        #Can only lose
#Bonus Round
    #Only if user has minimum winning in first 6 rounds
    #User picks secret prize from one letter in: OPULENCE
        #Prizes randomly generated from bonus bank
    #User given puzzle from remaining category.
        #Gets to guess ten letters.
            #Guess all before letters are shown
        #One chance to guess correctly
    #If user wins, bonus prize shown
        #Added to total
#User shown total winnings/prizes before prompted to exit.

#To-do:

import random

#Letter Banks
LETTERS = ("A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z",)
AN_LETTERS = ("A", "E", "F", "H", "I", "L","M",
              "N", "O", "R", "S", "X",) #For Grammar purposes

#Puzzle Banks
#Former & Latter Bank
FORM_LAT_BANK = ("SHOOTING FISH IN A BARREL OF LAUGHS!",
                 "THE WOLF OF WALL STREETCAR NAMED DESIRE",
                 "LOW-HANGING FRUIT BY THE FOOT",
                 "ALL THAT GLITTERS ISN'T GOLDENEYE",
                 "FIT AS A FIDDLER ON THE ROOF",
                 "BE THERE OR BE SQUARE DANCING")

#Verse Purse Bank
VERSE_BANK = ("WHY LAZE IN A CHAIR WHEN THERE'S A WORLD OUT THERE?!",
              "THE GREAT WALL IS ABOUT TWENTY FEET TALL",
              "A BIG MAN WITH A BIGGER PLAN",
              "TAKE A LOOK, IT'S IN A BOOK!",
              "SAM I AM IN GREEN EGGS AND HAM",
              "DON'T PANIC WHEN LIFE IS MANIC")

#Individual Bank
INDIV_BANK = ("PEACEFUL PROTESTER MAHATMA GANDHI",
              "FIRST FATHER FRED FLINTSTONE",
              "THE HIBACHI CHEF MAKING YOUR TERIYAKI BEEF",
              "BILL BIXBY AND LOU FERRIGNO AS THE INCREDIBLE HULK",
              "A BEEFEATER OUTSIDE BUCKINGHAM PALACE",
              "THE FOLKS SERVING DRINKS AT YOUR LOCAL DIVE",)

#Location Bank
LOC_BANK = ("A LITTLE CIGAR SHOP IN LITTLE HAVANA",
            "FIRST NATIONAL MONUMENT DEVILS TOWER",
            "RIPLEY'S BELIVE IT OR NOT! MUSEUM",
            "PIEDMONT PARK IN ATLANTA, GEORGIA",
            "THE LOCAL DELI WITH THE BEST PASTRAMI",
            "THE SEVEN WONDERS OF THE ANCIENT WORLD")

#Object Bank
OBJ_BANK = ("MOTHER'S FRESHLY COOKED CHERRY PIE",
            "A TASTY CLAW OF KING CRAB",
            "100 YEN, WHICH EQUALS ONE US DOLLAR",
            "SNORKEL AND GOGGLES USED TO SEE A CORAL REEF",
            "A PIECE OF HISTORY PRESERVED FOR GENERATIONS",
            "THE FAN SET TO HIGH ON A HOT SUMMER DAY")

#Notion Bank
NOTION_BANK = ("DOING NOTHING IS BETTER THAN BEING BUSY DOING NOTHING",
               "THE NEEDS OF THE MANY OUTWEIGH THE NEEDS OF THE FEW",
               "STRESSED? SPELL IT BACKWARDS FOR THE CURE",
               "LOSING AN ILLUSION MAKES YOU WISER THAN FINDING A TRUTH",
               "NO MAN IS A FAILURE WHO HAS FRIENDS",
               "MAY THE FORCE BE WITH YOU")

#Party On! Bank
PARTY_BANK = ("WEEKEND TRIPS WITH THE BEST BUDS",
              "HEY! HO! LET'S GO LISTEN TO BLITZKRIEG BOP!",
              "CATCHING A FREE CONCERT BY ROCK THE VOTE!",
              "THESE PRETZELS ARE MAKING ME THIRSTY!",
              "BEING PUT ON DOUBLE-SECRET PROBATION",
              "GASPARILLA PIRATE FESTIVAL IN TAMPA, FLORIDA")

#Circle Bank (24 total spots on "Circle")
C_BANK_USD_1 = (100, 250, 400, 550, 700, 850, 1000) #"2 Each On Circle"
C_BANK_USD_2 = (3000, 5000) #"One each on Circle"
C_BANK_OPT_1 = ("POVERTY", "PRIZE") #3 Each
C_BANK_OPT_2 = ("SAVE",) #2
C_BANK_PRIZE = (("A Trip to the Grand Canyon", 750),
                ("Crossfit Training Sessions", 175),
                ("A Brand New Laptop", 1150),
                ("A Portable Gaming Console", 200),
                ("A Week Stay in Jamaica", 2425),
                ("A Lifetime Supply of Pudding", 775),
                ("A Gift Card", 25),
                ("A Family Trip to Cancun", 4575),
                ("A JetSki", 8700),
                ("A Pair of Skis", 775),
                ("A Weekend Stay at Yellowstone", 350),
                ("A Vacation in Goa, India", 9875),
                ("A Michelin Star Meal", 225),
                ("An Extended Stay in California Wine Country", 6675))

#Bonus Prize Bank
BONUS_BANK = (50000, 50000, 75000, 75000, 100000, 100000, 500000, 1000000)

#Title Card
print("""
             C  I  R  C  L  E  !    O  F  !
                   
               O  P  U  L  E  N  C  E  !
      """)

print("\n\nBy Rich Williams")
input("\nPress Enter to Begin")

#Game Variables
winnings_total = 0
prizes_total = []
prizes_used = []
category_used = []
round_count = 0

#Game Loop
while round_count != 6:
    round_count += 1
    print("\n\nRound " + str(round_count) + "/6!")

    #Category Pick
    category_pick = random.randint(1, 7)
    while category_pick in category_used:
        category_pick = random.randint(1, 7)
    if category_pick == 1:
        category = "Category: Former & Latter"
        category_used += [category_pick]
        statement = random.choice(FORM_LAT_BANK)
    elif category_pick == 2:
        category = "Category: Verse Purse"
        category_used += [category_pick]
        statement = random.choice(VERSE_BANK)
    elif category_pick == 3:
        category = "Category: Individual(s)"
        category_used += [category_pick]
        statement = random.choice(INDIV_BANK)
    elif category_pick == 4:
        category = "Category: Location(s)"
        category_used += [category_pick]
        statement = random.choice(LOC_BANK)
    elif category_pick == 5:
        category = "Category: Object(s)"
        category_used += [category_pick]
        statement = random.choice(OBJ_BANK)
    elif category_pick == 6:
        category = "Category: Notion(s)"
        category_used += [category_pick]
        statement = random.choice(NOTION_BANK)
    elif category_pick == 7:
        category = "Category: Party On!"
        category_used += [category_pick]
        statement = random.choice(PARTY_BANK)
    else:
        print("error")

    #Puzzle Variables
    letters_used = []
    puzzle = ""
    winnings_round = 0
    prizes_round = []
    save = 0
    
    #Puzzle Loop
    while puzzle != statement:
        puzzle = ""
        puzzle_show = "" #puzzle/puzzle_show so player doesn't auto-win w/o answer

        #Puzzle Print with blanks
        for char in statement:
            if char in letters_used:
                puzzle_show += char
            elif char in LETTERS:
                puzzle_show += "_"
            else:
                puzzle_show += char
        print("\nPuzzle:")
        print("\n\n" + puzzle_show)
        print("\n" + category)
        print("\nWinnings: $" + str(winnings_round))
        if prizes_round:
            print("\nPrizes: ")
            for i, j in prizes_round:
                print(i, end="\n")
        if save > 0:
            print("\nSaves: " + str(save))

        #Player Options
        print("\n1: Rotate the Circle" +
              "\n2: Solve the Puzzle")
        option = input("Choice: ")
        while option != "1" and option != "2":
            option = input("Choice: ")

        #Rotate Circle
        if option == "1":
            spin = random.randint(1, 24)
            if spin > 0 and spin <= 14:
                result = random.choice(C_BANK_USD_1)
            elif spin > 14 and spin <= 16:
                result = random.choice(C_BANK_USD_2)
            elif spin > 16 and spin <= 22:
                result = random.choice(C_BANK_OPT_1)
            elif spin > 22 and spin <=24:
                result = random.choice(C_BANK_OPT_2)

            #POVERTY Spin
            if result == "POVERTY":
                if save >= 1:
                    print("\nRotation Result: POVERTY!")
                    print("You used a SAVE!")
                    save -= 1
                    continue
                else:
                    print("\nRotation Result: POVERTY!")
                    if winnings_round < 0: #Doubles Defecit if Negative
                        winnings_round *= 2
                        print("\nDebt Doubled!")
                    else:
                        winnings_round = 0
                if prizes_round:
                    print("\nPrizes Removed: ")
                    for i, j in prizes_round:
                        print(i, end="\n")
                    prizes_round = []
                continue

            #PRIZE, SAVE, and cash Spins
            elif result == "PRIZE":
                prize_pick = random.choice(C_BANK_PRIZE)
                while prize_pick in prizes_used:
                    prize_pick = random.choice(C_BANK_PRIZE)
                prizes_used += [prize_pick]
                print("\nRotation Result: PRIZE!")
                print("Guess a letter correctly to win!")
            elif result == "SAVE":
                print("\nRotation Result: SAVE!")
                print("Guess a letter correctly to win!")
            else:
                print("\nRotation Result: $" + str(result))

            #Guess Letter
            guess = input("\nGuess a Letter: ")
            guess = guess.upper()
            while guess not in LETTERS:
                guess = input("Guess a Letter: ")
                guess = guess.upper()

            #Already Guessed Letter: Results
            if guess in letters_used:
                print(guess + " was already guessed")
                if result == "PRIZE":
                    winnings_round -= prize_pick[1]
                    print("\nYou Missed: " + prize_pick)
                    print("Winnings Subtracted: $" + str(prize_pick[1]))
                elif result == "SAVE":
                    winnings_round //= 2
                    print("\nHalf of Winnings Lost!")
                else:
                    winnings_round -= result
                    print("\nWinnings Subtracted: $" + str(result))
                continue

            #Correct Guess/Results
            if guess in statement: 
                letter_count = 0 
                for i in statement:
                    if i == guess:
                        letter_count += 1
                if letter_count == 1:
                    if guess in AN_LETTERS:
                        print("An " + guess + " is present.")
                    else:
                        print("A " + guess + " is present.")
                elif letter_count > 1:
                    print("There are " + str(letter_count) + " " +
                          guess + "\'s present.")
                letters_used += guess
                if result == "PRIZE": #PRIZE Result
                    print("\nYou\'ve won: " + prize_pick[0] + "!")
                    prizes_round += [(prize_pick)]
                    print("Value: $" + str(prize_pick[1]))
                    winnings_round += prize_pick[1]
                elif result == "SAVE":#SAVE Result
                    print("\nYou won a SAVE!")
                    save += 1
                    print("Total Saves: " + str(save))
                else: #Cash Results
                    cash = result * letter_count
                    winnings_round += cash
                    print("\nWinnings Added: $" + str(cash))

            #Incorrect Guess                        
            else:
                print(guess + " is not present.")
                letters_used += guess
                if result == "PRIZE": #PRIZE Result
                    winnings_round -= prize_pick[1]
                    print("\nYou Lost: " + prize_pick[0])
                    print("Winnings Subtracted: $" + str(prize_pick[1]))
                elif result == "SAVE": #SAVE Result
                    if prizes_round:
                        safe_winnings = 0
                        for i, j in prizes_round:
                            safe_winnings += j
                        winnings_round -= (winnings_round - safe_winnings) // 2
                    else:
                        winnings_round //= 2
                    print("\nHalf of Winnings Subtracted")
                else: #Cash Result
                    winnings_round -= result
                    print("\nWinnings Subtracted: $" + str(result))

        #Chance to Solve
        elif option == "2":
            puzzle = input("\nThe answer is: ")
            puzzle = puzzle.upper()
            if puzzle != statement:
                print("Incorrect")
                if winnings_round > 0:
                    if prizes_round:
                        safe_winnings = 0
                        for i, j in prizes_round:
                            safe_winnings += j
                        winnings_round -= (winnings_round - safe_winnings) // 2
                    else:
                        winnings_round //= 2
                elif winnings_round < 0:
                    winnings_round *= 2
                else:
                    winnings_round = 0
            elif puzzle == statement:
                print("Correct!")

    #End of Round
    winnings_total += winnings_round
    prizes_total += prizes_round
    print("\nTotal winnings: $" + str(winnings_total))
    if prizes_total:
        print("\nPrizes Won:")
        for i, j in prizes_total:
            print(i, end="\n")
    if round_count < 6:
        input("\nNext Round!")
    else:
        input("\nRounds Complete!")

#Bonus Round
if winnings_total >= 42000:
    input("\nYour winnings are satisfactory for the Bonus Round!")
    BONUS_WORD = "OPULENCE"
    print("""
    Pick your Secret Prize:

    1: O
    2: P
    3: U
    4: L
    5: E
    6: N
    7: C
    8: E
          """)
    #Acceptable Bonus Picks
    B_PICKS = ("1", "2", "3", "4", "5", "6", "7", "8")
    bonus_pick = 0
    while bonus_pick not in B_PICKS:
        bonus_pick = input("Pick a Number: ")
    print("Your pick: " + BONUS_WORD[int(bonus_pick) - 1])

    #Bonus Category Pick
    category_pick = random.randint(1, 7)
    while category_pick in category_used:
        category_pick = random.randint(1, 7)
    if category_pick == 1:
        category = "Former & Latter"
        category_used += [category_pick]
        statement = random.choice(FORM_LAT_BANK)
    elif category_pick == 2:
        category = "Verse Purse"
        category_used += [category_pick]
        statement = random.choice(VERSE_BANK)
    elif category_pick == 3:
        category = "Individual(s)"
        category_used += [category_pick]
        statement = random.choice(INDIV_BANK)
    elif category_pick == 4:
        category = "Location(s)"
        category_used += [category_pick]
        statement = random.choice(LOC_BANK)
    elif category_pick == 5:
        category = "Object(s)"
        category_used += [category_pick]
        statement = random.choice(OBJ_BANK)
    elif category_pick == 6:
        category = "Notion(s)"
        category_used += [category_pick]
        statement = random.choice(NOTION_BANK)
    elif category_pick == 7:
        category = "Party On!"
        category_used += [category_pick]
        statement = random.choice(PARTY_BANK)
    else:
        print("error")

    #Bonus Puzzle
    puzzle_bonus = ""
    for char in statement:
        if char in LETTERS:
            puzzle_bonus += "_"
        else:
            puzzle_bonus += char

    print("\nBonus: Round 7!")
    print("\nPuzzle:", end="\n\n\n")
    print(puzzle_bonus)
    print("\n" + category, end="\n\n")

    #Bonus Letter Guesses
    letters_used = []
    while len(letters_used) < 7:
        guess = input("Pick a Letter: ")
        guess = guess.upper()
        while guess not in LETTERS:
            guess = input("Pick a Letter: ")
            guess = guess.upper()
        if guess in letters_used:
            print(guess + " was already picked")
            continue
        else:
            letters_used += guess
            if len(letters_used) == 6:
                print("\n" + str(7 - len(letters_used)) + " Pick Left")
            else:
                print("\n" + str(7 - len(letters_used)) + " Picks Left")

    #Bonus Puzzle w/ Guessed Letters
    puzzle_bonus = ""
    for char in statement:
        if char in letters_used:
            puzzle_bonus += char
        elif char in LETTERS:
            puzzle_bonus += "_"
        else:
            puzzle_bonus += char

    #Chance to Solve
    print("\nBonus Puzzle:", end="\n\n\n")
    print(puzzle_bonus)
    print("\n" + category, end="\n\n")
    print("Your Letters: ", end="")
    for i in letters_used:
        print(i, end=" ")

    answer = input("\n\n\nOne Chance to Solve: ")
    answer = answer.upper()

    #Correct Answer
    if answer == statement:
        print("Correct!")
        print("\nYour Secret Prize is: " + BONUS_WORD[int(bonus_pick) - 1])
        bonus_prize = random.choice(BONUS_BANK)
        input("\nYou Win... ")
        print("$" + str(bonus_prize) + "!!!!!!!")
        winnings_total += bonus_prize

    #Incorrect Answer
    elif answer != statement:
        print("Incorrect.")
        print("\nCorrect Answer:")
        print(statement)
        print("\nYour Secret Prize was: " + BONUS_WORD[int(bonus_pick) - 1])
        bonus_prize = random.choice(BONUS_BANK)
        input("\nYou could have won... ")
        print("$" + str(bonus_prize) + ".")
    else:
        print("error")
    
#No Bonus Round
else:
    print("\nYou did not win enough to play the Bonus Round.")

input("\n\nGame Complete!")
print("\nTotal winnings: $" + str(winnings_total))
print("\nPrizes Won:")
for i, j in prizes_total:
    print(i, end="\n")

input("\n\nThanks for Playing! Press Enter to Exit")
    
    
