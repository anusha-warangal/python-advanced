# Day 13: Student Marks Analyzer by Anusha
# Skills: Pandas, Matplotlib, CSV Handling

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Sample data create cheyadam - Dictionary tho
data = {
    'Name': ['Anusha', 'Priya', 'Ravi', 'Kiran', 'Divya'],
    'Roll': [1, 2, 3, 4, 5],
    'Maths': [95, 88, 76, 92, 85],
    'Science': [98, 90, 80, 95, 88],
    'English': [92, 85, 79, 90, 84]
}

# Step 2: DataFrame create chesi CSV lo save cheyadam
df = pd.DataFrame(data)
df.to_csv('Anusha_StudentMarks.csv', index=False)
print("✅ CSV File Create Ayyindi: Anusha_StudentMarks.csv\n")

# Step 3: CSV nunchi data chadavadi analysis cheyadam
df = pd.read_csv('Anusha_StudentMarks.csv')

# Total and Average add cheyadam
df['Total'] = df['Maths'] + df['Science'] + df['English']
df['Average'] = df['Total'] / 3

print("--- STUDENT MARKS REPORT ---")
print(df)
print("\n--- TOP PERFORMER ---")
top_student = df.loc[df['Total'].idxmax()]
print(f"Name: {top_student['Name']} | Total: {top_student['Total']} | Avg: {top_student['Average']:.2f}")

print("\n--- SUBJECT WISE AVERAGE ---")
print(f"Maths Avg: {df['Maths'].mean():.2f}")
print(f"Science Avg: {df['Science'].mean():.2f}")
print(f"English Avg: {df['English'].mean():.2f}")

# Step 4: Graph veyyadam - Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df['Name'], df['Total'], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
plt.title('Anusha Day 13 - Student Total Marks Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.ylim(0, 300)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Graph ni save cheyadam
plt.savefig('Anusha_MarksGraph.png')
print("\n✅ Graph Save Ayyindi: Anusha_MarksGraph.png")
plt.show()
