# Day 6: Functions - Reusable Code for DA

def calculate_average(marks_list):
    """
    This function takes a list of marks
    Returns total and average
    """
    total = 0
    for mark in marks_list:
        total = total + mark
    
    average = total / len(marks_list)
    return total, average  # Returns 2 values

# Test 1: Inter marks
inter_marks = [85, 90, 78, 92, 88]
total1, avg1 = calculate_average(inter_marks)
print("Inter Results:")
print(f"Total: {total1}, Average: {avg1}")

# Test 2: Mock test marks
mock_marks = [70, 75, 80, 65]
total2, avg2 = calculate_average(mock_marks)
print("\nMock Test Results:")
print(f"Total: {total2}, Average: {avg2}")

# DA use: Compare performance
if avg1 > avg2:
    print("\nInter marks are better than Mock")
else:
    print("\nMock test needs improvement")
