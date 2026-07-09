# ATM Simulator

balance = 10000
pin = "1234"

def check_balance():
    print(f"\n💰 Available Balance: ₹{balance:.2f}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f"✅ ₹{amount:.2f} deposited successfully.")
    else:
        print("❌ Invalid amount.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= 0:
        print("❌ Invalid amount.")
    elif amount > balance:
        print("❌ Insufficient balance.")
    else:
        balance -= amount
        print(f"✅ Please collect your cash: ₹{amount:.2f}")

def change_pin():
    global pin
    old_pin = input("Enter current PIN: ")
    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin:
            pin = new_pin
            print("✅ PIN changed successfully.")
        else:
            print("❌ PINs do not match.")
    else:
        print("❌ Incorrect current PIN.")

# Login
print("===== Welcome to Python ATM =====")
entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin == pin:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("🙏 Thank you for using our ATM!")
            break
        else:
            print("❌ Invalid choice. Try again.")
else:
    print("❌ Incorrect PIN. Access denied.")
