# Day 8: Reading CSV files = DS bread and butter

# Method 1: Basic file read
print("--- Method 1: Reading line by line ---")
file = open("marks.csv", "r") # r = read mode

for line in file:
    print(line.strip()) #.strip() removes \n

file.close() # Always close file

print("\n--- Method 2: Convert to Dict for DS ---")
# Better way for DS - convert each line to dictionary
data = [] # List to store all student dicts

file = open("marks.csv", "r")
header = file.readline().strip().split(",") # ['name','maths',...]
print("Columns:", header)

for line in file:
    values = line.strip().split(",") # ['Anusha','85','90'...]
    student = {} # Dict for 1 student
    for i in range(len(header)):
        student[header[i]] = values[i]
    data.append(student)

file.close()

# Now we have list of dicts = Like Pandas DataFrame
print("\nFull data:", data)
print("\nFirst student:", data[0])
print("Anusha Maths mark:", data[0]["maths"])

# DS Task: Calculate average of Maths for all students
maths_total = 0
for student in data:
    maths_total += int(student["maths"]) # Convert str to int

maths_avg = maths_total / len(data)
print(f"\nClass Maths Average: {maths_avg}")
