# Day 21 - map() Function

# Example 1: Square each number
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Numbers:", numbers)
print("Squares:", squares)


# Example 2: Double each number
numbers = [10, 20, 30, 40]

double = list(map(lambda x: x * 2, numbers))

print("Original:", numbers)
print("Doubled:", double)


# Practice
marks = [50, 60, 70, 80]

updated_marks = list(map(lambda x: x + 5, marks))

print("Marks:", marks)
print("Updated Marks:", updated_marks)