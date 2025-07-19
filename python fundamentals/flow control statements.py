# 1. Check if a given number is Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check if a given number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Check if two numbers have the same last digit
def lastDigit(a, b):
    if a % 10 == b % 10:
        print("true")
    else:
        print("false")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lastDigit(a, b)


# 4. Print numbers from 1 to 10 in a single row with tab space
for i in range(1, 11):
    print(i, end="\t")
print()


# 5. Print even numbers between 23 and 57
for i in range(23, 58):
    if i % 2 == 0:
        print(i)


# 6. Check if a number is prime
num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# 7. Print prime numbers between 10 and 99
for num in range(10, 100):
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num)


# 8. Sum of digits of a number
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits:", sum_digits)


# 9. Reverse a number
num = int(input("Enter a number to reverse: "))
reverse = 0
temp = num
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
print("Reversed number:", reverse)


# 10. Check if a number is palindrome
num = int(input("Enter a number to check for palindrome: "))
original = num
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10

if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")
