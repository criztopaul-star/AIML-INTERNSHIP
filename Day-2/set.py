# Create a set and print unique elements
s = {1, 2, 3, 4, 4, 5}

print("Unique elements in set:")
print(s)

# Add elements to a set
s.add(6)

print("\nAfter adding element:")
print(s)

# Remove elements from a set
s.remove(2)

print("\nAfter removing element:")
print(s)

# Create another set
s2 = {4, 5, 6, 7, 8}

# Perform union of two sets
print("\nUnion:")
print(s.union(s2))

# Perform intersection of two sets
print("\nIntersection:")
print(s.intersection(s2))

# Find difference between two sets
print("\nDifference:")
print(s.difference(s2))

# Check if element exists in set
if 3 in s:
    print("\n3 exists in set")
else:
    print("\n3 does not exist")

# Remove duplicates from list using set
list1 = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(list1))

print("\nList after removing duplicates:")
print(unique)

# Convert set to list
list2 = list(s)

print("\nSet converted to list:")
print(list2)

# Find symmetric difference between two sets
print("\nSymmetric Difference:")
print(s.symmetric_difference(s2))
