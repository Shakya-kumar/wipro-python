# -----------------------------------------------------------------------------------
# 1. Write a program to count the number of uppercase and lowercase letters in a string.
# -----------------------------------------------------------------------------------

text = input("Enter a string: ")
upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)


# -----------------------------------------------------------------------------------
# 2. Write a program that will check whether a given string is a palindrome or not.
# -----------------------------------------------------------------------------------

string = input("Enter a string to check palindrome: ")

if string == string[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


# -----------------------------------------------------------------------------------
# 3. Given a string, return a new string made of n copies of the first 2 chars of the 
# original string where n is the length of the string. Assume length >= 2.
# Example: "Wipro" → "WiWiWiWiWi"
# -----------------------------------------------------------------------------------

s = input("Enter a string (length >= 2): ")
n = len(s)
first_two = s[:2]
result = first_two * n
print("Result:", result)


# -----------------------------------------------------------------------------------
# 4. Given a string, if the first or last character is 'x', return the string without 
# those characters. Otherwise, return the string unchanged.
# Example: "xhix" → "hi"
# -----------------------------------------------------------------------------------

s = input("Enter a string: ")

if len(s) >= 1 and s[0] == 'x':
    s = s[1:]
if len(s) >= 1 and s[-1] == 'x':
    s = s[:-1]

print("Modified string:", s)


# -----------------------------------------------------------------------------------
# 5. Given a string and an integer n, return a string made of n repetitions of the 
# last n characters of the string.
# Example: "Wipro", 3 → "propropro"
# -----------------------------------------------------------------------------------

s = input("Enter a string: ")
n = int(input("Enter an integer (0 to length of string): "))

if 0 <= n <= len(s):
    end_part = s[-n:]
    result = end_part * n
    print("Result:", result)
else:
    print("Invalid value of n.")
