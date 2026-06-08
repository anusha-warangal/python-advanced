# Day 8 Project - CSV Marks Analyzer by Anusha
# Built during 30 Day Data Science Challenge

students = {
    "Anusha": [85, 90, 78],
    "Ravi": [92, 88, 95],
    "Priya": [76, 84, 89]
}

# Calculate average for each student
for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(f"{name}: Average = {avg:.2f}")

# Find class topper
topper = max(students, key=lambda x: sum(students[x]))
print(f"Class Topper: {topper}")
