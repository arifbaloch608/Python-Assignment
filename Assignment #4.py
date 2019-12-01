# Q:1 Use a dictionary to store information about a person you know. Store their first name, last name, age,
# and the city in which they live. You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary. Add a new key value pair about qualification then
# update the qualification value to high academic level then delete it.

Asif = {"first name": "Asif", "last name": "Khayanr", "age": "24", "city": "karachi"}


print(Asif["first name"])
print(Asif["last name"])
print(Asif["age"])
print(Asif["city"])
Asif["Qualification"] = "Graduation"
print(Asif)
del Asif["Qualification"]
print(Asif)

# Q:2 Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city. The keys for each city’s dictionary should be something
# like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {"Karachi": ["Pakistan", "15,741,406", "It is the Sixth largest city in the world by city population"],
          "Hyderabad": ["Pakistan", "5,734,601",
                        "It is the second-largest city in Sindh and fourth-largest in Pakistan"],
          "Sehwan": ["Pakistan", "1,176,969.", "Sehwan is one of the oldest towns of the province of Sindh, in "
                                               "Pakistan. It is highly respected in interior Sindh, well known for "
                                               "the resting place of the great mystic poet, saint and scholar, "
                                               "Lal Shahbaz Qalandar, who lived here in 13th century."]}

print(cities["Karachi"])
print(cities["Hyderabad"])
print(cities["Sehwan"])

# Q:3 A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3,
# the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

i = True
while i:
    age = int(input("Enter Your Age:"))
    if 0 < age < 3:
        print("The Ticket Is Free")
    elif 3 <= age <= 12:
        print("The ticket is $10")
    elif age >= 12:
        print("The ticket is $15")
    else:
        print("incorect key")
        i = False


# Q:4 Write a function called favorite_book() that accepts one parameter, title. The function should
# print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(title):
    if title == "Alice":
        print("One of my favorite books is Alice in Wonderland")


favorite_book("Alice")

# Q:5 Guess the number game
# Write a program which randomly generate a number between 1 to 30 and ask the user in input field to guess
# the correct number. Give three chances to user guess the number and also give hint to user if hidden
# number is greater or smaller than the number he given to input field.

import random
random_no = random.randint(1, 30)
guess = 0
g_over = False
number = int(input('Enter Guess Number:'))
while not g_over:

    if number == random_no:
        print(f'winner , you trying {guess} times')
        g_over = True
    else:
        if number < random_no:
            print('too  low')

        else:
            print('Too High')
        guess += 1
        if guess == 3:
            print(f"Your {guess} chances Over  ")
            g_over = True
            break
        number = int(input('Enter Guess Number:'))

