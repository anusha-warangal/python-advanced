# Day 10 - Find max number
# Author: Anusha

marks = [85, 90, 78, 92, 88]
largest = marks[0] # assume first is largest

for mark in marks:
    if mark > largest:
        largest = mark # update if bigger found

print("Marks:", marks)
print("Highest mark =", largest)
