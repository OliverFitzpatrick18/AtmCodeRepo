import random

#creates a random number between 1000 and 9999, will be the users pin
def users_pin():
    return str(random.randint(1000, 9999))

#for the sake of testing, money in the account is randomised
def users_balance():
    return int(random.randint(1, 1000))

pin = users_pin()

balance = users_balance()
#this print pin is for testing purposes only so i can enter the account
print(pin)

pin_input = input("Enter your pin:")

history_dict = {}



while pin_input == pin:

    repeat = 1
    
    while repeat == 1:
        options = {0: "0 = check balance",
                   1: "1 = withdraw money",
                   2: "2 = Deposit money",
                   3: "3 = view transation history",
                   4: "4 = withdraw card" }

        for key, value in options.items():
            print(f"{key}: {value}")

        user_choice = input("What would you like to do today = ")

        if user_choice == "0":
            print("the balance of the account is", balance)
        elif user_choice == "1":
            amount = int(input("how much do you want to take out = "))
            if amount <= balance:
                balance = balance - amount
                print(amount, "has been withdrawn")
                history_dict[len(history_dict) + 1] = f"£{amount} has been withdrawn; Current balance: £{balance}"
            else:
                print(amount, "not enough money in the account, please remove the card")
        elif user_choice == "2":
            amount = int(input("how much do you want to put into the account: "))
            balance = balance + amount
            print("the current balance is now", balance)
            history_dict[len(history_dict) + 1] = f"£{amount} has been deposited; Current balance: £{balance}"
        elif user_choice == "3":
            for key, value in history_dict.items():
                print(f"{key}: {value}")   
        elif user_choice == "4":
            print("please take your card")
        else:
            print("service not available, please choose another")
    
        break
    
    repeat = input("1=Yes 0=No do you require another service: ")

    if repeat == "0":
        print("Please remove your card")#
        break





