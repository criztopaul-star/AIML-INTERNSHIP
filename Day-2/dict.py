# Create a dictionary and print keys and values
student = {
    "name": "Georgie",
    "age": 20,
    "mark": 95
}

print("Dictionary:")
print(student)

print("\nKeys:")
print(student.keys())

print("\nValues:")
print(student.values())

# Add a new key-value pair
student["course"] = "Python"

print("\nAfter adding new key-value pair:")
print(student)

# Update value of existing key
student["mark"] = 98

print("\nAfter updating mark:")
print(student)

# Delete a key from dictionary
del student["age"]

print("\nAfter deleting age:")
print(student)

# Check if a key exists
if "name" in student:
    print("\nKey 'name' exists")
else:
    print("\nKey 'name' does not exist")

# Loop through dictionary items
print("\nDictionary items:")

for key, value in student.items():
    print(key, ":", value)

# Merge two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)

print("\nMerged dictionary:")
print(d1)

# Find maximum value in dictionary
marks = {
    "A": 50,
    "B": 90,
    "C": 75
}

print("\nMaximum value:")
print(max(marks.values()))

# Count frequency of elements using dictionary
list1 = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for i in list1:
    freq[i] = freq.get(i, 0) + 1

print("\nFrequency count:")
print(freq)

# Create nested dictionary and access values
students = {
    "student1": {
        "name": "John",
        "mark": 90
    },
    "student2": {
        "name": "Alice",
        "mark": 95
    }
}

print("\nNested dictionary:")
print(students)

print("\nAccessing value:")
print(students["student1"]["name"])
