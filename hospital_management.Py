patients = {}

while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Count Patients")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")
        patient_name = input("Enter Patient Name: ")

        patients[patient_id] = patient_name
        print("Patient added successfully!")

    elif choice == "2":
        if not patients:
            print("No patient records found!")
        else:
            print("\nPatient Records:")
            for patient_id, patient_name in patients.items():
                print(f"ID: {patient_id}, Name: {patient_name}")

    elif choice == "3":
        patient_id = input("Enter Patient ID to search: ")

        if patient_id in patients:
            print("Patient Name:", patients[patient_id])
        else:
            print("Patient not found!")

    elif choice == "4":
        print("Total Patients:", len(patients))

    elif choice == "5":
        print("Exiting Hospital Management System...")
        break

    else:
        print("Invalid choice!")
