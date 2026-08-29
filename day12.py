fruits = ["Apple", "Banana", "Mango"]

print("Original:", fruits)

fruits.append("Orange")
print("After append:", fruits)

fruits.insert(1, "Grapes")
print("After insert:", fruits)

fruits.remove("Banana")
print("After remove:", fruits)

fruits.pop()
print("After pop:", fruits)

print("Total items:", len(fruits))