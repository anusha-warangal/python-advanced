products = {}

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Count Products")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        products[product_name] = quantity
        print("Product added successfully!")

    elif choice == "2":
        if not products:
            print("No products available!")
        else:
            print("\nInventory:")
            for product, quantity in products.items():
                print(f"{product} - Quantity: {quantity}")

    elif choice == "3":
        product_name = input("Enter product name to search: ")

        if product_name in products:
            print(f"Quantity: {products[product_name]}")
        else:
            print("Product not found!")

    elif choice == "4":
        print("Total Products:", len(products))

    elif choice == "5":
        print("Exiting Inventory Management System...")
        break

    else:
        print("Invalid choice!")
