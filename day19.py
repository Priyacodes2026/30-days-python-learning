# Day 19 - Functions with Multiple Parameters

# Student details function
def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_details("Priya", 21, "Biomedical Engineering")


# Addition function
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Addition:", result)


# Calculate total
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(100, 3)
print("Total Price:", total)