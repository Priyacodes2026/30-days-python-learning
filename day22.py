# Day 22 - filter() Function

# Example 1: Even numbers
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Numbers:", numbers)
print("Even Numbers:", even_numbers)


# Example 2: Marks greater than 50
marks = [35, 60, 45, 80, 90]

passed_marks = list(filter(lambda x: x >= 50, marks))

print("Marks:", marks)
print("Passed Marks:", passed_marks)


# Practice
ages = [15, 18, 21, 16, 25]

adults = list(filter(lambda x: x >= 18, ages))

print("Ages:", ages)
print("Adults:", adults)