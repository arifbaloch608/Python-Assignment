# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


number = int(input("Input a number to compute the factiorial : "))

print(factorial(number))

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


def calculatealphabets(s):
    upperltrs = 0
    lowerltrs = 0
    for c in s:
        if c.isupper():
            upperltrs += 1
        elif c.islower():
            lowerltrs += 1
        else:
           pass
    print("Original String : ", s)
    print("Number. of Upper case characters : ", upperltrs)
    print("Number. of Lower case Characters : ", lowerltrs)


calculatealphabets('The quick Brown Fox')
# Write a Python function to print the even numbers from a given list


def evenNumber(Givenlist):
    list = []
    for n in Givenlist:
        if n % 2 == 0:
            list.append(n)
    return list


print(evenNumber([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam


def PalindromeorNot(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


print(PalindromeorNot('arif'))
# Write a Python function that takes a number as a parameter and check the number is prime or not


def IsPrimeOrNot(number):
    if (number == 1):
        return False
    elif (number == 2):
        return True;
    else:
        for x in range(2, number):
            if(number % x == 0):
                return False
        return True


print(IsPrimeOrNot(7))
# Suppose a customer is shopping in a market and you need to print all the items which user bought from market.
# Write a function which accepts the multiple arguments of user shopping list and
# print all the items which user bought from market.


def shopping(*shoppintlist):
    print("Item which bought:")
    for item in shoppintlist:
        print(item)


shopping("Soap", "Shampoo", "Paste", "Toothbrush")
