books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Count Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if not books:
            print("No books available!")
        else:
            print("\nBooks in Library:")
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book}")

    elif choice == "3":
        search = input("Enter book name to search: ")

        if search in books:
            print("Book found!")
        else:
            print("Book not found!")

    elif choice == "4":
        print("Total Books:", len(books))

    elif choice == "5":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice!")
