balance=50000
while True:
    print("Welcome to our ATM")
    print("\n===ATM MEnu===")
    print("1.Check balance")
    print("2.Money Withdraw")
    print("3.Cash Deposit")
    print("4.Exit")

    choice=input("Enter your input(1/2/3/4): ")
    if choice == '1':
        print(f"Your current balance is {balance}")
    elif choice == '2':
        amount= float(input("Enter the amount: "))
        if 0<amount<balance:
            balance -= amount
            print(f"Balance is withdrawn{balance}")
            print(f"Current balance is {balance}")
        else:
            print("Invalid Input.Please enter amount correctly")
    elif choice == '3':
        amount= float(input("Enter the amount: "))
        if amount > 0 :
            balance += amount
            print(f"Balance is deposited {amount}")
            print(f"Current balance is {balance}")
        else:
            print("Invalid Input. Please enter amount correctly")
    elif choice == '4':
        print("Thank You For using ATM")

        break
    else:
        print("Invalid Choice! Please Select 1,2,3, or 4")


