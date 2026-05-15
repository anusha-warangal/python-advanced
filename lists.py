# Day 5: Lists and Loops - DA Foundation

# List = Like array in C. Stores multiple values.
marks = [85, 90, 78, 92, 88]  # 5 subjects
total = 0

print("Your marks:", marks)

# For loop to add all marks
for mark in marks:  # Takes each value from list
    total = total + mark

average = total / len(marks)  # len() gives count = 5

print(f"Total marks: {total}")
print(f"Average: {average}")

# DA logic: Grade calculation
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
else:
    print("Grade: C")
