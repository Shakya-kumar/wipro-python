# -----------------------------------------------------------------------------------
#
# Project 1:
# Write a program to accept numbers as command line arguments 
# and display their sum.
#
# Example:
# Command: python program.py 10 20 30
# Output: Sum = 60
# -----------------------------------------------------------------------------------

import sys

def sum_all_arguments():
    args = sys.argv[1:]
    if not args:
        print("No numbers provided.")
        return
    numbers = list(map(int, args))
    print("Sum =", sum(numbers))


# -----------------------------------------------------------------------------------
# Project 2:
# Write a program to accept a welcome message through command line arguments 
# and display the file name along with the welcome message.
#
# Example:
# Command: python program.py Welcome to Python
# Output:
# File Name: program.py
# Message: Welcome to Python
# -----------------------------------------------------------------------------------

def display_welcome_message():
    if len(sys.argv) < 2:
        print("Please provide a welcome message.")
        return
    message = " ".join(sys.argv[1:])
    print("File Name:", sys.argv[0])
    print("Message:", message)


# -----------------------------------------------------------------------------------
# Project 3:
# Write a program to accept 10 numbers through command line arguments 
# and calculate the sum of prime numbers among them.
#
# Example:
# Command: python program.py 2 3 4 5 6 7 8 9 10 11
# Output: Sum of prime numbers: 28
# (Prime numbers: 2, 3, 5, 7, 11 → 28)
# -----------------------------------------------------------------------------------

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_primes_from_arguments():
    args = sys.argv[1:]
    if len(args) != 10:
        print("Please provide exactly 10 numbers.")
        return
    numbers = list(map(int, args))
    prime_sum = sum(num for num in numbers if is_prime(num))
    print("Sum of prime numbers:", prime_sum)


