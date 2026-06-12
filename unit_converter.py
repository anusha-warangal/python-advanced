# Day 31 Project 30: Unit Converter
# Author: Ellaboina Anusha - BSc CS 1st Year

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def kg_to_pounds(kg):
    return kg * 2.20462

def main():
    print("=== DAY 32: UNIT CONVERTER ===")

    while True:
        print("\n1. KM to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. KG to Pounds")
        print("4. Exit")

        choice = input("Select 1-4: ")

        if choice == '1':
            km = float(input("Enter KM: "))
            print(f"{km} KM = {km_to_miles(km):.2f} Miles")

        elif choice == '2':
            c = float(input("Enter Celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")

        elif choice == '3':
            kg = float(input("Enter KG: "))
            print(f"{kg} KG = {kg_to_pounds(kg):.2f} Pounds")

        elif choice == '4':
            print("Thank you! 💜")
            break
        else:
            print("Invalid choice!")

main()
