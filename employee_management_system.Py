employees = {}

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Count Employees")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Employee Name: ")

        employees[emp_id] = emp_name
        print("Employee added successfully!")

    elif choice == "2":
        if not employees:
            print("No employee records found!")
        else:
            print("\nEmployee Records:")
            for emp_id, emp_name in employees.items():
                print(f"ID: {emp_id}, Name: {emp_name}")

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in employees:
            print("Employee Name:", employees[emp_id])
        else:
            print("Employee not found!")

    elif choice == "4":
        print("Total Employees:", len(employees))

    elif choice == "5":
        print("Exiting Employee Management System...")
        break

    else:
        print("Invalid choice!")
