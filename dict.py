# Day 7: Dictionaries = Labels + Values = DS foundation

# Why dict > list?
# List: marks = [85, 90, 78] → What subject is 90?
# Dict: marks = {"Maths": 85, "Physics": 90} → Clear

student = {
    "name": "Anusha",
    "course": "MSCs",
    "year": 1,
    "marks": [85, 90, 78, 92, 88], # List inside dict
    "city": "Huzurabad"
}

# 1. Access values
print("Name:", student["name"])
print("First subject mark:", student["marks"][0])

# 2. Add new key = Add new column in DS
student["avg"] = sum(student["marks"]) / len(student["marks"])
student["grade"] = "A" if student["avg"] >= 85 else "B"

# 3. Update value
student["year"] = 2 # Promoted

# 4. Loop through all keys = Read full row
print("\n--- Student Record ---")
for key, value in student.items():
    print(f"{key}: {value}")

# 5. Check if key exists = Safety in DS
if "phone" in student:
    print("Phone:", student["phone"])
else:
    print("Phone not added yet")

# 6. Delete key
# del student["city"] # If not needed
