# Day 18: Student Grade Calculator - Anusha from Warangal
# Saves result to file like real projects

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

def save_to_file(name, marks, grade):
    with open("student_results.txt", "a") as file:
        file.write(f"Name: {name}, Marks: {marks}, Grade: {grade}\n")
    print("Result saved to student_results.txt ✅")

# Main program
print("=== Day 18: Grade Calculator ===")
student_name = input("Enter student name: ")
student_marks = int(input("Enter marks out of 100: "))

student_grade = calculate_grade(student_marks)

print(f"\n--- Result ---")
print(f"Student: {student_name}")
print(f"Marks: {student_marks}/100")
print(f"Grade: {student_grade}")

save_to_file(student_name, student_marks, student_grade)
print("\nDay 18 complete! 🔥")
