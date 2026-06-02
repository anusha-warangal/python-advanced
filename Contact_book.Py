contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found!")
        else:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found!")

    elif choice == "4":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice!")
