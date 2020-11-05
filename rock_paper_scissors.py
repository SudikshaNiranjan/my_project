import random
from time import sleep

choice = ["Rock", "Paper ", "Scissors"]
computer = random.choice(choice)

player = False

while player == False:
    print("Welcome to Rock, Paper and Scissors")
    print("\nPlease wait, The game is loading.....")
    sleep(3)
    player = input("Which one do you want to choose?\n'Rock'= 'Rock'\n'Paper'= 'Paper'\n'Scissors' 'Scissors'\n'Stop the game'= 'Stop': ")
    if player == computer:
        print("\nPlease wait, We are loading your results....")
        sleep(2)
        print("It's a tie")
    elif player == "Rock":
        if computer == "Paper":
            print("\nPlease wait, We are loading your results....")
            sleep(2)
            print("You have lost!!")
        else:
            print("\nPlease wait, We are loading your results....")
            sleep(2)
            print("You have Won!!")
    elif player == "Scissors":
        if computer == "Rock":
            print("\nPlease wait, We are loading your results....")
            sleep(2)
            print("You have lost!!")
        else:
            print("\nPlease wait, We are loading your results....")
            sleep(2)
            print("You have Won!!")
    elif player == "Paper":
        if computer == "Scissors":
            print("\nPlease wait, We are loading your results....")
            sleep(2)
            print("You have lost!!")
        else:
            print("\nPlease wait, We are loading your results....")
            sleep(2)
            print("You have Won!!")
    elif player =="Stop":
        print("Thank you for playing Rock, Paper and Scissors!!")
        break
    else:
        print("That is not a valid play, Spelling mistake has occured")
        break

    player = False
