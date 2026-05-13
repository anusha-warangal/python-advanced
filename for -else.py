# Day 1 - for...else prime checker
num = 29
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is NOT prime")
        break
else:
    print(f"{num} is PRIME")  # This runs
