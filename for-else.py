# Day 2 Python - For-Else Loop
# Anusha's 100 Days of Code

print("=== For-Else Demo ===")

num = int(input("Enter a number: "))
def prime(num):
        if num <= 1:
                print(f"{num} is not a prime number")
                return
                
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not prime")
                break
        else:
            print(f"{num} is a prime number")
        
prime(num)

print("Day 2 Python Complete - Logic unlocked")
