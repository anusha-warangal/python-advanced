import csv

FILE_NAME = "students.csv"


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student Added Successfully!\n")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n--- Student Records ---")
            for row in reader:
                print(f"Roll No: {row[0]}, Name: {row[1]}, Marks: {row[2]}")
            print()

    except FileNotFoundError:
        print("No records found.\n")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            found = False
            for row in reader:
                if row[0] == roll:
                    print("\nStudent Found")
                    print(f"Roll No: {row[0]}")
                    print(f"Name: {row[1]}")
                    print(f"Marks: {row[2]}\n")
                    found = True
                    break

            if not found:
                print("Student Not Found\n")

    except FileNotFoundError:
        print("No records found.\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    rows = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] != roll:
                    rows.append(row)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Student Deleted Successfully!\n")

    except FileNotFoundError:
        print("No records found.\n")


def update_marks():
    roll = input("Enter Roll Number: ")
    new_marks = input("Enter New Marks: ")

    rows = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == roll:
                    row[2] = new_marks
                rows.append(row)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Marks Updated Successfully!\n")

    except FileNotFoundError:
        print("No records found.\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice\n")
