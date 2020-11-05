import random

def login():
  print("Welcome to Guess the Number!!")
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")

  if username == "Sudiksha" and password == "2010":
    print("Correct, You have successfully logged into the application")
    return True
  else:
    print("You have entered the wrong login details, Atuthentication Failed")
    return False

def start_game():
  if login():
    number = random.randint(1,10)
    chances = 0

    while chances < 10:
      print("The random number has been generated")
      guess = int(input("Guess the number: "))
      chances = chances + 1

      if guess == number:
        print("Congratulations, You have guessed the right number and won the game!!")
        break

      elif guess < number:
        print("The number you guessed is a number more than the given number")
      elif guess > number:
        print("The number you guessed is a number less than the given number")

    if chances > 10:
      print("Sorry, You have run out of chances, GAME OVER")

start_game()
