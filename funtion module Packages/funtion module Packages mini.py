# -----------------------------------------------------------------------------------
# Stream: Python
# Tech Module: Functions / Modules / Packages
# Project: 1
#
# Write a Python function that accepts a hyphen-separated sequence of colors as input 
# and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
#
# Constraint:
# - All the colors will be completely in either lower case or upper case.
#
# Sample Input 1:
# green-red-yellow-black-white
#
# Sample Output 1:
# black-green-red-white-yellow
#
# Sample Input 2:
# PINK-BLUE-TAN-PURPLE
#
# Sample Output 2:
# BLUE-PINK-PURPLE-TAN
# -----------------------------------------------------------------------------------


def sort_colors_alphabetically(color_string):
    """
    Accepts a hyphen-separated string of color names,
    sorts them alphabetically, and returns the sorted string.
    """
    color_list = color_string.split('-')
    color_list.sort()
    return '-'.join(color_list)


input_colors = input("Enter hyphen-separated colors: ")
sorted_colors = sort_colors_alphabetically(input_colors)
print("Sorted colors:", sorted_colors)

# -----------------------------------------------------------------------------------
# Stream: Python
# Tech Module: Functions / Modules / Packages
# Project: 2
#
# Create a Python program that defines and uses the following functions:
#
# 1. Function Name: is_palindrome(name)
#    - Task: Given the user name as input, this function should tell us 
#      whether the name is a palindrome or not.
#
# 2. Function Name: count_vowels(name)
#    - Task: Given the user name as input, this function should tell us 
#      how many vowels are present in it.
#
# 3. Function Name: frequency_of_letters(name)
#    - Task: Given the user name as input, this function should tell us 
#      how many times each letter appears in the name.
#    - Note: The name will be completely in either lower case or upper case.
#
# After defining the above functions, call them by accepting user input
# and print the output in the format shown below.
#
# Sample Input 1: bob
# Sample Output 1:
# Yes, it is a palindrome
# No of vowels: 1
# Frequency of letters: b-2, o-1
#
# Sample Input 2: marcel bentok tanaka
# Sample Output 2:
# No, it is not a palindrome
# No of vowels: 7
# Frequency of letters: a-4, b-1, c-1, e-2, k-2, l-1, m-1, n-2, o-1, r-1, t-1
# -----------------------------------------------------------------------------------


def is_palindrome(name):
    """Check if the given string is a palindrome."""
    if name == name[::-1]:
        return "Yes, it is a palindrome"
    else:
        return "No, it is not a palindrome"


def count_vowels(name):
    """Count and return the number of vowels in the given string."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return f"No of vowels: {count}"


def frequency_of_letters(name):
    """Return a string representing the frequency of each letter (excluding spaces)."""
    freq = {}
    for char in name:
        if char != ' ':  # ignore spaces
            freq[char] = freq.get(char, 0) + 1

    result = "Frequency of letters: "
    for key in sorted(freq.keys()):
        result += f"{key}-{freq[key]}, "
    return result.rstrip(', ')


name = input("Enter a name: ")

print(is_palindrome(name))
print(count_vowels(name))
print(frequency_of_letters(name))
