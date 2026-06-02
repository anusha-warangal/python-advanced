passwords = {}

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account = input("Enter account name: ")
        password = input("Enter password: ")

        passwords[account] = password
        print("Account added successfully!")

    elif choice == "2":
        if not passwords:
            print("No accounts saved!")
        else:
            print("\nSaved Accounts:")
            for account, password in passwords.items():
                print(f"{account}: {password}")

    elif choice == "3":
        account = input("Enter account name to search: ")

        if account in passwords:
            print("Password:", passwords[account])
        else:
            print("Account not found!")

    elif choice == "4":
        print("Exiting Password Manager...")
        break

    else:
        print("Invalid choice!")
