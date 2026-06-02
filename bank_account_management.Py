balance = 0

while True:
    print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Current Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"₹{amount} deposited successfully!")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using the Bank System!")
        break

    else:
        print("Invalid choice!")
