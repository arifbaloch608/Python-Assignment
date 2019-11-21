# Q:1 Write a program which takes 5 inputs from user for different subject’s marks,
# total it and generate mark sheet using grade?

print("Enter marks obtained in 5 subjects: ")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())
Total = mark1 + mark2 + mark3 + mark4 + mark5
average = (Total / 500) * 100
if average >= 90 and average <= 100:
    print("Your Grade is A+")
elif average>= 80 and average <90:
    print("Your Grade is A")
elif average>=70 and average<80:
    print("Your Grade is B")
elif average>=60 and average<70:
    print("Your Grade is C")
elif average>=50 and average<60:
    print("Your Grade is F")
else:
    print("Your Grade is F")

# Q:2 Write a program which take input from user and identify that the given number is even or odd?
num = input("Enter any number: ")
number = float(num)
check = number % 2
if check == 0:
    print(int(number), "is an even number.")
else:
    print(int(number), "is an odd number.")


# Q:3 Write a program which print the length of the list?
listofnumbers = [1, 4, 5, 7, 8, 6]
print("The length of list is: ", len(listofnumbers))

# Q:4 Write a Python program to sum all the numeric items in a list?

lst = [1, 4, 5, 7, 8, 6, 6]
numbers = 0
for n in lst:
    numbers = numbers+n
print("Sum of elements in given list is :", numbers)

# Q:5 Write a Python program to get the largest number from a numeric list
list1 = [10, 20, 4, 45, 9]
print("Largest element is:", max(list1))


# 6. Take a list, say for example this one:
#    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for n in a:
    if n < 5:
        print(n)
