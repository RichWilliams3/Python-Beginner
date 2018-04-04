#Cryptoquip
#
#By Rich Williams
#
#
#Outline:
#
#1. Title Card
#2. Code Bank
#3. Quip Bank
#4. Round Loop
    #While Player wants to continue playing, loop continues
    #Round Loop: sections 4-12
#5. Letter Encryption
    #Each letter of alphabet assigned a new letter as code
        #No duplicates
    #No repeats
    #Make sure different
#6. Quip Selection and Encryption
    #Quip selected from quip bank
    #Each letter encrypted from code determined by Letter Encryption section
#7. Hint Selection
    #Vowels that are in the quip are added to a hint bank
#8. Puzzle Section
    #puzzle is printed, along with one, random hint from the hint bank.
    #Users are given the option to Answer, get a Hint, or Yield.
    #Users can earn points per round. Total score is kept.
    #Puzzle Loop: sections 8-12
#9. Answer Option
    #Users given chance to input puzzle answer.
    #If the answer is exactly equal to the quip, the loop exits
    #User awarded points based on how many hints used
    #If incorrect, kicks back to beginning of Puzzle Loop
#10. Yield Option
    #If user gives up, the quip is printed
#11. Hint section
    #A random, unique hint from the hint bank is selected
    #Once all hints used, hint option removed
#12. Play Again
    #If user plays again, restarts Round Loop
        #AKA new encryption, new quip, etc.
    #If user ends game, total score from all rounds is printed
    #Used quips tracked. If all quips used, game ends automatically.

#Concepts Used:
#Tuples
#Lists
#random.choice()
#for loops
#in operator
#continue
#len()

#1. Title Card
print("\n\t\t\tC  R  Y  P  T  O  Q  U  I  P")
print("\t\t       / \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\/ \\")
print("\t\t       \\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /")
print("\t\t\tM  C  V  A  E  S  B  I  Q  A")
print("\n\n\nBy Rich Williams")
input("\nPress Enter to Begin")

#Imports
import random

#2. Code Bank
CODE_BANK = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
             "Y", "Z")

#3. Quip Bank
QUIP_BANK = ("IF PATRICK IS IN A BAD MOOD, WOULD HE BE A KRABBY PATTY?",
             "AN ESKIMO WALKS INTO THE STORE. HE'S A PRETTY COOL CUSTOMER.",
             "IF YOU BUY A FISH IN POLAND, WAS IT CAUGHT BY A FISHING POLE?",
             "EARN FAVOR WITH CAPRICORN FOR A CURRIED GOAT",
             "DOES A SECRETIVE SQUID SPRAY INVISIBLE INK?",
             "A DETECTIVE INVESTIGATES A BLIMP, MAKING IT A LEAD ZEPPELIN.",
             "RABBITS SHOULD BE DOCTORS. THEY'D PROVIDE A SPEEDY RECOVERY!",
             "MY FRIEND SAYS I'M A PILL. THIS MAKES ME HARD TO SWALLOW.",
             "AN APPLE A DAY KEEPS THE FRUIT INDUSTRY PROFITABLE",
             "WOULD AN ENTHUSIASTIC ECONOMIST BE HIGH ON SUPPLY?",
             "FOLKS SAY A MALE FIREFLY IS A PRETTY BRIGHT GUY",
             "ELEPHANTS NEVER FORGET A SPARE TIRE BECAUSE THEY HAVE A LOT OF TRUNK SPACE",
             "DRINK LOTS OF EARL GREY ON MARIJUANA TO ENJOY A POT-TEA BREAK",
             "I EAT ICE CREAM FOR HOURS AT WEEK'S END. DON'T JUDGE MY LAZY SUNDAE!",
             "SOCIAL FOLK CAN NEVER BE TEXAS SINGERS. IT'S THE LONE-STAR STATE.",
             "E-MAIL? G-MAIL? I MISS THE GOOD OLD DAYS WHERE I-MAIL U-MAIL.",
             "A PERSON WHO KEEPS YOU FROM CLEANING YOUR CLOTHES IS A LAUNDRY HAMPER-ER",
             "DOES A PUGILIST IN A SMALL RING EVER FEEL BOXED IN?",
             "DON'T FRET WHILE INQUIRING ABOUT THE CARNIVAL. IT'S A FARE QUESTION.",
             "A SIMPERING SOMMELIER HAS A REAL TASTE FOR WHINE...",
             "IF YOUR DOG SHEDS IN YOUR VEHICLE, YOU SHOULD GET A CAR-PET CARPET.",
             "TERRIBLE COMEDIANS USUALLY PROVIDE A BARREL OF GAFFES.",
             "MY BROTHER DRINKS A LOT OF WATER. I CALL HIM MY H-2-BRO.",
             "I'M A COMPUTER EXPERT. PEOPLE SAY I'M THE CONTROL-ALT-ELITE.",
             "NOTHING RHYMES WITH ORANGE... EXCEPT MAYBE DOOR-HINGE!",
             "I KNOW THE KEYS TO SUCCESS, BUT I SUFFER FROM BAD LOCK.",
             "MARGARINE ISN'T BAD, BUT THE REAL STUFF IS BUTTER.",
             "WOULD YOU CALL A FOOTBALL PLAYER'S PREVIOUS FOUL PAST-INTERFERENCE?",
             "IS A WOODCHUCK THAT WON'T CHUCK WOOD CALLED A WONTCHUCK?",
             "IF FREUD IS NEARLY PERFECT, DOES THAT MEAN HE'S ACHIEVED SIX-SIGMUND?",
             "A FRIEND ONCE TOLD A MISCHEVIOUS LAD FROM THE E.U., \"EUROPE TO NO GOOD!\"",
             "A FLATMATE IN NEED IS A FRIEND IN-DEED",
             "GRANDPA FINALLY GOT HIS COLLEGE DEGREE! HE WAS A SENIOR SENIOR.",
             "IF A GOLFER CHEATED TO SHOOT TWO UNDER PAR, IT WAS AN ILLEGAL EAGLE.",
             "WOULD A NERDY SWINDLER CAN USUALLY BE FOUND AT COMIC-CON?",
             "RANDOMLY SEEING AN ALIEN IS A CHANCE ENCOUNTER OF THE THIRD KIND",
             "ECHOES ARE NICE. IF YOU CALL, THEY ALWAYS CALL BACK",
             "IS THE PRESIDENT OF THE A.D.A. REQUIRED TO TAKE AN OATH OF ORIFICE?",
             "THERE WAS A RIOT AT MCDONALDS! IT WAS LIKE LORD OF THE FRIES!",
             "IF YOUR HEADPHONES AREN'T TOO LOUD, THEY'RE YOUR EAR-BUDS",
             "WHICH OCEAN IS THE BEST? ASK THE MOON. IT'S THE TIDE-BREAKER.",
             "DOLPHINS LOVE FRENCH CINEMA BECAUSE THE END IS ALWAYS 'FIN'",)

quip_bank_used = []

#4. Round Loop
score_total = 0
again = ""
while again != "N":
    code_bank_used = []
#5. Letter Encryption
    #Crypto A
    new_a = "A"
    while new_a == "A":
        while new_a == "A" or new_a in code_bank_used:
            new_a = random.choice(code_bank)
        code_bank_used += new_a
    #Crypto B
    new_b = "B"
    while new_b == "B":
        while new_b == "B" or new_b in code_bank_used:
            new_b = random.choice(code_bank)
        code_bank_used += new_b
    #Crypto C
    new_c = "C"
    while new_c == "C":
        while new_c == "C" or new_c in code_bank_used:
            new_c = random.choice(code_bank)
        code_bank_used += new_c
    #Crypto D
    new_d = "D"
    while new_d == "D":
        while new_d == "D" or new_d in code_bank_used:
            new_d = random.choice(code_bank)
        code_bank_used += new_d
    #Crypto E
    new_e = "E"
    while new_e == "E":
        while new_e == "E" or new_e in code_bank_used:
            new_e = random.choice(code_bank)
        code_bank_used += new_e
    #Crypto F
    new_f = "F"
    while new_f == "F":
        while new_f == "F" or new_f in code_bank_used:
            new_f = random.choice(code_bank)
        code_bank_used += new_f

    #Crypto G
    new_g = "G"
    while new_g == "G":
        while new_g == "G" or new_g in code_bank_used:
            new_g = random.choice(code_bank)
        code_bank_used += new_g
    #Crypto H
    new_h = "H"
    while new_h == "H":
        while new_h == "H" or new_h in code_bank_used:
            new_h = random.choice(code_bank)
        code_bank_used += new_h

    #Crypto I
    new_i = "I"
    while new_i == "I":
        while new_i == "I" or new_i in code_bank_used:
            new_i = random.choice(code_bank)
        code_bank_used += new_i
    #Crypto J
    new_j = "J"
    while new_j == "J":
        while new_j == "J" or new_j in code_bank_used:
            new_j = random.choice(code_bank)
        code_bank_used += new_j

    #Crypto K
    new_k = "K"
    while new_k == "K":
        while new_k == "K" or new_k in code_bank_used:
            new_k = random.choice(code_bank)
        code_bank_used += new_k
    #Crypto L
    new_l = "L"
    while new_l == "L":
        while new_l == "L" or new_l in code_bank_used:
            new_l = random.choice(code_bank)
        code_bank_used += new_l
    #Crypto M
    new_m = "M"
    while new_m == "M":
        while new_m == "M" or new_m in code_bank_used:
            new_m = random.choice(code_bank)
        code_bank_used += new_m

    #Crypto N
    new_n = "N"
    while new_n == "N":
        while new_n == "N" or new_n in code_bank_used:
            new_n = random.choice(code_bank)
        code_bank_used += new_n
    #Crypto O
    new_o = "O"
    while new_o == "O":
        while new_o == "O" or new_o in code_bank_used:
            new_o = random.choice(code_bank)
        code_bank_used += new_o
    #Crypto P
    new_p = "P"
    while new_p == "P":
        while new_p == "P" or new_p in code_bank_used:
            new_p = random.choice(code_bank)
        code_bank_used += new_p
    #Crypto Q
    new_q = "Q"
    while new_q == "Q":
        while new_q == "Q" or new_q in code_bank_used:
            new_q = random.choice(code_bank)
        code_bank_used += new_q
    #Crypto R
    new_r = "R"
    while new_r == "R":
        while new_r == "R" or new_r in code_bank_used:
            new_r = random.choice(code_bank)
        code_bank_used += new_r
    #Crypto S
    new_s = "S"
    while new_s == "S":
        while new_s == "S" or new_s in code_bank_used:
            new_s = random.choice(code_bank)
        code_bank_used += new_s
    #Crypto T
    new_t = "T"
    while new_t == "T":
        while new_t == "T" or new_t in code_bank_used:
            new_t = random.choice(code_bank)
        code_bank_used += new_t
    #Crypto U
    new_u = "U"
    while new_u == "U":
        while new_u == "U" or new_u in code_bank_used:
            new_u = random.choice(code_bank)
        code_bank_used += new_u
    #Crypto V
    new_v = "V"
    while new_v == "V":
        while new_v == "V" or new_v in code_bank_used:
            new_v = random.choice(code_bank)
        code_bank_used += new_v
    #Crypto W
    new_w = "W"
    while new_w == "W":
        while new_w == "W" or new_w in code_bank_used:
            new_w = random.choice(code_bank)
        code_bank_used += new_w
    #Crypto X
    new_x = "X"
    while new_x == "X":
        while new_x == "X" or new_x in code_bank_used:
            new_x = random.choice(code_bank)
        code_bank_used += new_x
    #Crypto Y
    new_y = "Y"
    while new_y == "Y":
        while new_y == "Y" or new_y in code_bank_used:
            new_y = random.choice(code_bank)
        code_bank_used += new_y
    #Crypto Z
    new_z = "Z"
    while new_z == "Z":
        while new_z == "Z" or new_z in code_bank_used:
            new_z = random.choice(code_bank)
        code_bank_used += new_z

#6. Quip Selection and Encryption
    quip = random.choice(quip_bank)
    while quip in quip_bank_used:
        quip = random.choice(quip_bank)
    quip_bank_used += [quip]    
    puzzle = ""
    for char in quip:
        if char == "A":
            puzzle += new_a
        elif char == "B":
            puzzle += new_b
        elif char == "C":
            puzzle += new_c
        elif char == "D":
            puzzle += new_d
        elif char == "E":
            puzzle += new_e
        elif char == "F":
            puzzle += new_f
        elif char == "G":
            puzzle += new_g
        elif char == "H":
            puzzle += new_h
        elif char == "I":
            puzzle += new_i
        elif char == "J":
            puzzle += new_j
        elif char == "K":
            puzzle += new_k
        elif char == "L":
            puzzle += new_l
        elif char == "M":
            puzzle += new_m
        elif char == "N":
            puzzle += new_n
        elif char == "O":
            puzzle += new_o
        elif char == "P":
            puzzle += new_p
        elif char == "Q":
            puzzle += new_q
        elif char == "R":
            puzzle += new_r
        elif char == "S":
            puzzle += new_s
        elif char == "T":
            puzzle += new_t
        elif char == "U":
            puzzle += new_u
        elif char == "V":
            puzzle += new_v
        elif char == "W":
            puzzle += new_w
        elif char == "X":
            puzzle += new_x
        elif char == "Y":
            puzzle += new_y
        elif char == "Z":
            puzzle += new_z
        else:
            puzzle += char

#7. Hint Selection
    hint_bank = []
    if new_a in puzzle:
        hint_bank += [new_a + " = A / "]
    if new_e in puzzle:
        hint_bank += [new_e + " = E / "]
    if new_i in puzzle:
        hint_bank += [new_i + " = I / "]
    if new_o in puzzle:
        hint_bank += [new_o + " = O / "]
    if new_u in puzzle:
        hint_bank += [new_u + " = U / "]
    if new_y in puzzle:
        hint_bank += [new_y + " = Y / "]
    hint_pick = random.choice(hint_bank)
    hint_count = 1
    hint = hint_pick

#8. Puzzle Section
    score_round = 0
    answer = ""
    while answer != quip:
        option = ""
        while option != "A" and option != "H" and option != "Y":
            print("\n" + puzzle)
            print("\nHints:", end="\n")
            print(hint)
            if hint_count < len(hint_bank):
                option = input("\n\nType \'A\' to Answer. Type \'H\' for a Hint. " +
                           "Type \'Y\' to Yield. (A/H/Y): ")
            else:
                option = input("\n\nType \'A\' to Answer. Type \'Y\' to Yield. (A/Y): ")
            option = option.upper()

            #9. Answer Option         
            if option == "A":
                answer = input("\nPrint Answer: ")
                answer = answer.upper()
                if answer == quip:
                    print("Correct!")
                    if hint_count >= 1 and hint_count < len(hint_bank):
                        score_round += (2 + len(hint_bank)) - hint_count
                        score_total += score_round
                    elif hint_count == len(hint_bank):
                        score_round += 1
                        score_total += score_round
                    else:
                        print("error")
                    print("\nScore this Round: " + str(score_round))
                elif answer != quip:
                    print("Incorrect")
            #10. Yield Option
            elif option == "Y":
                print(quip)
                print("\nScore this Round: 0")
                answer = quip
            #11. Hint Option
            elif option == "H":
                if hint_count < len(hint_bank):
                    hint_pick = random.choice(hint_bank)
                    while hint_pick in hint:
                        hint_pick = random.choice(hint_bank)
                    hint += hint_pick
                    hint_count += 1
                else:
                    continue

#12. Play Again
    if len(quip_bank) == len(quip_bank_used):
        print("\n\nOut of Quips! Sorry!")
        again = "N"
    else: 
        again = input("\n\nPlay again? (Y/N): ")
        again = again.upper()

print("\nTotal Score: " + str(score_total))
input("\n\nThanks for Playing! Press Enter to Exit")
