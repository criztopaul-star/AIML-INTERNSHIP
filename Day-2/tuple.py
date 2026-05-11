# Create a tuple and print elements
t = (10, 20, 30, 40, 20)

print("Tuple elements:")
for i in t:
    print(i)

# Convert tuple to list and modify it
l = list(t)
l.append(50)

print("\nModified list:", l)

# Count occurrences of an element in tuple
count = t.count(20)
print("\nCount of 20:", count)

# Find index of an element in tuple
index = t.index(30)
print("\nIndex of 30:", index)

# Concatenate two tuples
t2 = (60, 70)

new_tuple = t + t2

print("\nConcatenated tuple:", new_tuple)

# Slice a tuple
print("\nSliced tuple:", new_tuple[1:4])

# Check if element exists in tuple
if 40 in t:
    print("\n40 exists in tuple")
else:
    print("\n40 does not exist")

# Find length of tuple
print("\nLength of tuple:", len(t))

# Convert list to tuple
list1 = [1, 2, 3]

tuple1 = tuple(list1)

print("\nList converted to tuple:", tuple1)

# Iterate through tuple elements
print("\nIterating through tuple:")

for item in new_tuple:
    print(item)
