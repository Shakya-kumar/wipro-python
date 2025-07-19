# -----------------------------------------------------------------------------------
# Stream: Python
# Tech Module: Command Line Arguments
# Project: 1
#
# Through command line arguments, three strings separated by space are given to you.
# Each string is a series of numbers separated by hyphen(-).
#
# - You like all the numbers in string 1.
# - You dislike all the numbers in string 2.
# - The third string contains the numbers given to you.
# - Your initial happiness is 0.
#
# Task:
# When you encounter a number which is present in string 1 (likes), add 1 to happiness.
# When you encounter a number which is present in string 2 (dislikes), subtract 1 from happiness.
# If the number is not in string 1 or 2, happiness remains unchanged.
#
# Print the final happiness score.
#
# Sample input 1:
# Command: python program.py 3-1 5-7 1-5-3-8
# Output: 1
#
# Explanation:
# - Like list: 3, 1 → +1 for 1 and +1 for 3 = 2
# - Dislike list: 5, 7 → -1 for 5 = 1
# - 8 is ignored
#
# Sample input 2:
# Command: python program.py 60-77-345-244-11-99-3 77-15-13-2-34-3 77-2-34-3-15-13
# Output: 2
#
# Explanation:
# - Like: 60, 77, 345, 244, 11, 99, 3 → +1 for 77, 2, 34 = +3
# - Dislike: 77, 15, 13, 2, 34, 3 → -1 for 3 = -1
# - Final happiness = 2
# -----------------------------------------------------------------------------------

import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python program.py <likes> <dislikes> <given_numbers>")
        return

 
    likes_str = sys.argv[1]
    dislikes_str = sys.argv[2]
    given_str = sys.argv[3]

  
    likes = set(map(int, likes_str.split('-')))
    dislikes = set(map(int, dislikes_str.split('-')))
    given_numbers = list(map(int, given_str.split('-')))

    happiness = 0


    for num in given_numbers:
        if num in likes:
            happiness += 1
        elif num in dislikes:
            happiness -= 1

   
    print(happiness)

if __name__ == "__main__":
    main()
