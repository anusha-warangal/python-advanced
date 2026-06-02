expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded!")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. ₹{expense}")

    elif choice == "3":
        print("Total Expense: ₹", sum(expenses))

    elif choice == "4":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice!")
