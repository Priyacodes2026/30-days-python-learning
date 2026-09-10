# Day 20 - Lambda Functions

# Normal function
def square(number):
    return number * number

print("Normal Function:", square(5))


# Lambda function
square_lambda = lambda number: number * number

print("Lambda Function:", square_lambda(5))


# Addition using Lambda
add = lambda a, b: a + b

print("Addition:", add(10, 20))


# Multiplication using Lambda
multiply = lambda a, b: a * b

print("Multiplication:", multiply(5, 4))