students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        students[roll_no] = name
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found!")
        else:
            print("\nStudent Records:")
            for roll_no, name in students.items():
                print(f"Roll No: {roll_no}, Name: {name}")

    elif choice == "3":
        roll_no = input("Enter Roll Number to search: ")

        if roll_no in students:
            print("Student Name:", students[roll_no])
        else:
            print("Student not found!")

    elif choice == "4":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice!")
