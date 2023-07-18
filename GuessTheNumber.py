import random

Game = "Guess the number."
Game_Bold = '\x1B[1m' + Game + '\x1B[0m'

print("Welcome to "+ Game_Bold+".")
print("There are two Different Gamemodes.\n1 - You Guess the Number Bot Picks.\n2 - The Bot Guesses the Number You Pick.")
Gamemode3 = 0
while Gamemode3 == 0:
    try:
        Gamemode4 = int(input("Pick Gamemode ( 1 or 2 ) : "))
    except Exception:
        print("Enter Numbers only.")
    if Gamemode4 >= 1 and Gamemode4 <= 2:
        Gamemode3 = Gamemode4

while Gamemode3 != 0:
    if Gamemode3 == 1:    
        print("There are different levels of difficulty.\n1 - Difficulty 'Easy'    has 10 tries.\n2 - Difficulty 'Medium'  has 7 tries.\n3 - Difficulty 'Hard'    has 5 tries.\n4 - Difficulty 'Extreme' has 3 tries.")
        Gamemode = 0
        while Gamemode == 0:
            try:
                Gamemode2 = int(input("Enter Difficulty ( 1-4 ) : "))
            except Exception:
                print("Enter Number only.")
            if Gamemode2 >= 1 and Gamemode2 <= 4:
                Gamemode = Gamemode2

        tries = 0
        if Gamemode == 1:
            tries += 9
        elif Gamemode == 2:
            tries += 6
        elif Gamemode == 3:
            tries += 4
        elif Gamemode == 4:
            tries += 2

        print("You Have "+ str(tries+1) +" tries.")

        x = random.randint(1,100)
        try:
            i = int(input("Enter an integer between 1 to 100 : "))
            if i > 100 or i < 1:
                i = input("Number has to be between 1 and 100 : ")
        except Exception:
            print("Enter Numbers only.")

        while i != x and tries > 0: 
            if i > x:
                print("Wrong!!, The number is smaller than "+ str(i) +".")
            else: 
                print("Wrong!!, The number is larger than "+ str(i) +".")
            tries -= 1
            try:
                i = int(input("Try Again!! : "))
            except Exception:
                print("Enter Number only.")

        if i == x:
            print("Correct!!, The Number was "+ str(x)+".")
        elif tries <= 0:
            print("Out Of tries.")

    elif Gamemode3 == 2:
        Valid = "No"
        while Valid == "No":
            try:
                Number = int(input("Enter the Number you want the Bot to guess (1 to 100) : "))
            except Exception:
                print("Enter Numbers only.")
            if Number >= 1 and Number <= 100:
                Valid = "Yes"
            else:
                print("Number not Valid!! ")

        Confirm = ""
        Min = 1
        Max = 100
        while Confirm != "Y":
            Bot_Move = random.randint(Min,Max)
            print("Is the Number "+ str(Bot_Move) +".")
            try:
                print(Min)
                print(Max)
                Confirm = input("Type L for Lower, H for Higher or Y If It Is Correct : ")
            except Exception:
                print("Only Enter H, L or Y")
            Confirm_Lower = Confirm.lower()
            if Confirm_Lower == "l":
                Max = Bot_Move
            elif Confirm_Lower == "h":
                Min = Bot_Move
            elif Confirm == "y":
                print("Yay, the bot Guessed it!!")
                break
    
    print("Do you want to play again?")
    print("Y for Yes, N for No")
    try:
        Exit = input(": ")
    except Exception:
        print("Enter Y or N ONLY.")
    Exit_Lower = Exit.lower()
    if Exit_Lower == "n":
        Gamemode3 = 0
        break
    elif Exit_Lower == "y":
        print("Select Gamemode Again.")
        print("1 - You Guess the Number Bot Picks.\n2 - The Bot Guessed the Number You Pick.")
        Valid3 = "No"
        while Valid3 == "No":
            try:
                Gamemode4 = int(input("Which Gamemode? (1 or 2) : "))
            except Exception:
                print("Enter 1 or 2 ONLY.")
            if Gamemode4 >= 1 and Gamemode4 <= 2:
                Valid3 = "Yes"
                Gamemode3 = Gamemode4

print("Goodbye, Thankyou for playing the Game.")




    



        
        
