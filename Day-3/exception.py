# 1. Take user input and safely convert it to integer
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid integer input")


# 2. Division calculator with error handling
try:
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")


# 3. Access list elements safely
try:
    l = [10, 20, 30, 40]
    index = int(input("\nEnter index: "))
    print("Element:", l[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Invalid index")


# 4. Open file and handle file not found
try:
    f = open("sample.txt", "r")
    print("\nFile opened successfully")
except FileNotFoundError:
    print("\nFile not found")


# 5. Login system with custom exception
class LoginError(Exception):
    pass

username = "admin"
password = "1234"

for i in range(3):
    u = input("\nEnter username: ")
    p = input("Enter password: ")

    try:
        if u == username and p == password:
            print("Login successful")
            break
        else:
            raise LoginError("Invalid login")
    except LoginError as e:
        print(e)


# 6. Convert string to float
try:
    x = float(input("\nEnter float value: "))
    print("Float value:", x)
except ValueError:
    print("Invalid float input")


# 7. ATM withdrawal with insufficient balance handling
balance = 5000

try:
    amount = int(input("\nEnter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient balance")

    balance -= amount

    print("Remaining balance:", balance)

except Exception as e:
    print(e)


# 8. Validate age with custom exception
class AgeError(Exception):
    pass

try:
    age = int(input("\nEnter age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above")

    print("Valid age")

except AgeError as e:
    print(e)

except ValueError:
    print("Invalid age input")


# 9. Handle multiple exceptions
try:
    num1 = int(input("\nEnter number: "))
    num2 = int(input("Enter another number: "))

    print(num1 / num2)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Division by zero not allowed")


# 10. Use finally to ensure file closing
try:
    file = open("sample.txt", "r")
    print("\nFile opened")

except FileNotFoundError:
    print("\nFile not found")

finally:
    try:
        file.close()
        print("File closed")
    except:
        pass
