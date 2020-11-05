import random
from time import sleep

choices = ["Charmander", "Squirtle", "Balbasur"]

computer = random.choice(choices)

player = False

name = input("Hello, Please enter your name: ")

while player == False:
    print(f"Hello, {name}. Welcome to the Pokemon Battles Game!!")
    player = input("Which pokemon do you want to choose?\n'Charmander': 'Charmander'\n'Squirtle': 'Squirtle'\n'Bulbasur': 'Bulbasur'\n'Stop the game': 'Stop': ")
    if player == computer:
        print("Tie!!")

    elif player == "Charmander":
        if computer == "Squirtle":
            print("\nPlease wait, we are loading your results....")
            sleep(1)
            print("You have lost!!")
        else:
            print("\nPlease wait, we are loading your results....")
            sleep(1)
            print("You have Won!!")

    elif player == "Squirtle":
        if computer == "Balbasur":
            print("\nPlease wait, we are loading your results....")
            sleep(1)
            print("You have lost!!")
        else:
            print("\nPlease wait, we are loading your results....")
            sleep(1)
            print("You have Won!!")

    elif player == "Balbasur":
        if computer == "Charmander":
            print("\nPlease wait, we are loading your results....")
            sleep(1)
            print("You have lost!!")
        else:
            print("\nPlease wait, we are loading your results....")
            sleep(1)
            print("You have Won!!")

    elif player == "Stop":
        print("Thank you for playing Pokemon Battles Game!!")
        break
    else:
        print("That is not a valid play, Spelling mistake has occured!")
        break

    player = False
