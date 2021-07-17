import random

randNum = random.randint(0,100)
userInputList = []
print("\n**************************** Welcome to the Guess Game (by shubham) ************************")
print("\n********************** Let's begin the game! ****************************\n")
user_input = int(input("Please make a guess for the number: "))
while user_input != randNum:
    if user_input < randNum:
        print("Please guess a higher number! \n")
        userInputList.append(user_input)
        user_input = int(input("Please make a guess for the number: "))
    if user_input > randNum:
        print("Please guess a lower number! \n")
        userInputList.append(user_input)
        user_input = int(input("Please make a guess for the number: "))

if user_input==randNum:
    print(f"Congratulations! {randNum} was the number!")
    userInputList.append(user_input)
print("\n*********************** Game Over! ********************************\n")

print(f"The total number of guesses you made = {len(userInputList)}")



with open("highscore.txt", 'r') as highscore:
        read_highscore= int(highscore.read())

if read_highscore <= len(userInputList): 
    print(f"The high score is: {read_highscore}")

if read_highscore > len(userInputList):
    print(f"The previous high score: {read_highscore}")
    print("Congratulation! You have made the new high score!")
    with open("highscore.txt", 'w') as highscore:
        highscore.write(str(len(userInputList)))
    with open("highscore.txt", 'r') as highscore:
        read_highscore=int(highscore.read())
    print(f"The new high score: {read_highscore}")



