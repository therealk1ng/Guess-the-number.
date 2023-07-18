Game = "Guess the number."
Game_Bold = '\x1B[1m' + Game + '\x1B[0m'

print("Welcome to "+ Game_Bold+".")
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

import random
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