import sys
import datetime

# Q-1 : Write a Python program to print the following string in a specific format (see the output).

print('Twinkle, twinkle, little star,\n'
      '\t  How I wonder what you are!\n'
      '\t\t\tUp above the world so high,\n'
      '\t\t\tLike a diamond in the sky.\n'
      'Twinkle, twinkle, little star,\n'
      '\t  How I wonder what you are')

# Q-2: Write a Python program to get the Python version you are using?

print(sys.version)

# Q-3:Write a Python program to display the current date and time?

print(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S %t'))


# Q-4. Write a Python program which accepts the radius of a circle from the user and compute the area.
radius_of_circle = float(input('Write a Radius of Circle:'))

print("Area of Circle: "+radius_of_circle**2 * 3.14)

# Q-5. Write a Python program which accepts the user's first and last name and print them in reverse
# order with a space between them?

fname = input('First Name:')
lname = input('Last Name:')

print(lname+" "+fname)

# Q-6. Write a python program which takes two inputs from user and print them addition

num_1 = int(input("Enter Number 1:"))
num_2 = int(input("Enter Number 2:"))
#
print(f"Addition of {num_1} + {num_2} is {num_1+num_2}")
