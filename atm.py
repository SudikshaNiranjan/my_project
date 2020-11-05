from time import sleep

def password():
  pin = int(input("Please, Enter your account pin: "))
  if pin == 2010:
      print("Correct account, Please we are fetching you data...")
      sleep(2)
      return True
  else:
      print("Incorrect pin, Authentication Failed!!")
      return False


def atm_start():

  balance = 0

  print("Welcome to SUDIKSHA'S ATM!!")
  if password():
    while True:
      print("Press '1' for Checking Balance")
      print("Press '2' for Withdrawal")
      print("Press '3' for Deposit")
      print("Press '4' for Exiting the ATM")

      choose = int(input("\nChoose which money transaction that fits for your day: "))

      if choose == 1:
          print("Please wait we are fetching you data...")
          sleep(2)
          print("Your account balance is: ", balance)

      elif choose == 2:
          withdrawal = int(input("How much money do you want to take from you account: "))
          balance = balance - withdrawal
          print(f"You have successfully taken {withdrawal} money from your account")

      elif choose == 3:
          deposit = int(input("How much money do you want to add to your account: "))
          balance = balance + deposit
          print(f"You have succesfully added {deposit} money to you account")

      elif choose == 4:
          print("Thanks for using SUDIKSHA'S ATM, Hope you have a good day!!")
          break


atm_start()
