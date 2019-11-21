# Q:1 Make a calculator using Python with addition , subtraction , multiplication , division and power.
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


def power(x, y):
    return x **y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
# Take input from the user
choice = input("Enter choice(1/2/3/4): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    print(num1, "power", num2, "=", power(num1, num2))
else:
    print("Invalid input")


# Q:2 Write a program to check if there is any numeric value in list using for loop

def isNumber(s):
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
    return True
#
#
lst = [10, 20, 4, "asd", 9]
for num in lst:
    if isNumber(str(num)):
        print(num, "Integer")


# Q:3  Write a Python script to add a key to a dictionary

dict = {'key1': 'value1', 'key2': 'value2'}
print("Current Dict is: ", dict)

dict.update({'key3': 'value3'})
print("Updated Dict is: ", dict)

# Q:4 Write a Python program to sum all the numeric items in a dictionary

def returnSum(myDict):
    sum = 0
    for i in myDict:
        if isNumber(str(myDict[i])):
            sum = sum + myDict[i]
    return sum


dict = {'a': 100, 'b': 200, 'c': "abc"}
print("Sum :", returnSum(dict))

# Q:5 Write a program to identify duplicate values from list
my_list = [20, 30, 20, 10, 5, 5]
my_list.sort()
for i in range(len(my_list) - 1):
    if my_list[i] == my_list[i+1]:
        print(my_list[i])

# Q:6 Write a Python script to check if a given key already exists in a dictionary

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


print("Enter key:")
is_key_present(int(input()))
