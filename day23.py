# Day 23 - reduce() Function

from functools import reduce

# Example 1: Add all numbers
numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print("Numbers:", numbers)
print("Total:", total)


# Example 2: Multiply all numbers
numbers = [1, 2, 3, 4]

product = reduce(lambda a, b: a * b, numbers)

print("Numbers:", numbers)
print("Product:", product)


# Practice
marks = [10, 20, 30, 40]

total_marks = reduce(lambda a, b: a + b, marks)

print("Marks:", marks)
print("Total Marks:", total_marks)