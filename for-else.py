# Day 2 Python - For-Else Loop
# Anusha's 100 Days of Code

print("=== For-Else Demo ===")

for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} IS PRIME")  # runs if no break happened

print("Day 2 Python Complete - Logic unlocked")
