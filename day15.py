# Day 15 - Dictionary Methods

student = {
    "name": "Priya",
    "age": 21,
    "course": "Biomedical Engineering"
}

# keys() - all keys
print("Keys:", student.keys())

# values() - all values
print("Values:", student.values())

# items() - key + value pairs
print("Items:", student.items())

# get() - particular value
print("Name:", student.get("name"))

# update() - add/update data
student.update({"age": 22, "city": "Chennai"})
print("Updated Dictionary:", student)