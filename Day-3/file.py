# 1. Write 10 user names into a file
f = open("users.txt", "w")

for i in range(1, 11):
    name = input("Enter username: ")
    f.write(name + "\n")

f.close()

print("\n10 usernames written to file")


# 2. Read file and filter specific words
f = open("users.txt", "r")

print("\nNames containing letter 'a':")

for line in f:
    if "a" in line:
        print(line.strip())

f.close()


# 3. Count words, lines, and characters
f = open("users.txt", "r")

data = f.read()

words = len(data.split())
characters = len(data)

f.seek(0)

lines = len(f.readlines())

print("\nLines:", lines)
print("Words:", words)
print("Characters:", characters)

f.close()


# 4. Append data without overwriting
f = open("users.txt", "a")

f.write("NewUser\n")

f.close()

print("\nData appended successfully")


# 5. Create log file with timestamps
from datetime import datetime

log = open("log.txt", "a")

log.write(str(datetime.now()) + " - Program executed\n")

log.close()

print("\nLog written")


# 6. Copy content between files
f1 = open("users.txt", "r")
f2 = open("copy.txt", "w")

f2.write(f1.read())

f1.close()
f2.close()

print("\nFile copied")


# 7. Remove duplicate lines
f = open("users.txt", "r")

lines = f.readlines()

unique = list(set(lines))

f.close()

f = open("unique.txt", "w")

f.writelines(unique)

f.close()

print("\nDuplicate lines removed")


# 8. Store and calculate student marks
f = open("marks.txt", "w")

total = 0

for i in range(3):
    mark = int(input("\nEnter mark: "))
    total += mark
    f.write(str(mark) + "\n")

average = total / 3

print("Average:", average)

f.close()


# 9. Parse CSV-like file manually
f = open("data.txt", "w")

f.write("John,20\n")
f.write("Alice,22\n")

f.close()

f = open("data.txt", "r")

print("\nParsed data:")

for line in f:
    name, age = line.strip().split(",")
    print("Name:", name, "Age:", age)

f.close()


# 10. Update records inside file
f = open("data.txt", "r")

lines = f.readlines()

f.close()

f = open("data.txt", "w")

for line in lines:
    if "John" in line:
        f.write("John,25\n")
    else:
        f.write(line)

f.close()

print("\nRecord updated")
