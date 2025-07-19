# -----------------------------------------------------------------------------------
# 1. Write a function to return the sum of all numbers in a list.
# Sample List: [8, 2, 3, 9, 7]
# Expected Output: 29
# -----------------------------------------------------------------------------------

def sum_of_list(numbers):
    return sum(numbers)

print("Sum of list:", sum_of_list([8, 2, 3, 9, 7]))


# -----------------------------------------------------------------------------------
# 2. Write a function to return the reverse of a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"
# -----------------------------------------------------------------------------------

def reverse_string(s):
    return s[::-1]

print("Reversed string:", reverse_string("1234abcd"))


# -----------------------------------------------------------------------------------
# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).
# Sample Input: 5
# Expected Output: 120
# -----------------------------------------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial:", factorial(5))


# -----------------------------------------------------------------------------------
# 4. Write a function that accepts a string and prints the number of uppercase 
# and lowercase letters in it.
# Sample Input: "Hello World"
# Expected Output: Uppercase: 2, Lowercase: 8
# -----------------------------------------------------------------------------------

def count_case_letters(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_case_letters("Hello World")


# -----------------------------------------------------------------------------------
# 5. Write a function to print the even numbers from a given list.
# The list is passed to the function as an argument.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]
# -----------------------------------------------------------------------------------

def print_even_numbers(lst):
    evens = [num for num in lst if num % 2 == 0]
    print("Even numbers:", evens)

print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])


# -----------------------------------------------------------------------------------
# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
# Sample Input: 7
# Expected Output: 7 is a prime number
# -----------------------------------------------------------------------------------

def is_prime(num):
    if num <= 1:
        return f"{num} is not a prime number"
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return f"{num} is not a prime number"
    return f"{num} is a prime number"

print(is_prime(7))
