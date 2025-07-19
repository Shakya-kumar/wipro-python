
# 1. Write a program to read the entire content from a txt file and display it to the user.
def read_entire_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print("Entire file content:")
        print(content)


# 2. Write a program to read first n lines from a txt file. Get n as user input.
def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        print(f"First {n} lines from the file:")
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line.strip())


# 3. Write a program to accept input from user and append it to a txt file.
def append_to_file(filename):
    user_input = input("Enter text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(user_input + '\n')
    print("Text appended successfully.")


# 4. Write a program to read contents from a txt file line by line and store each line into a list.
def read_lines_into_list(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
        print("Lines stored in list:")
        print(lines)


# 5. Write a program to find the longest word from the txt file contents,
#    assuming that the file will have only one longest word in it.
def find_longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        longest = max(words, key=len)
        print("Longest word in the file:", longest)


# 6. Write a program to count the frequency of a user-entered word in a txt file.
def count_word_frequency(filename):
    search_word = input("Enter a word to count its frequency: ")
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        frequency = words.count(search_word)
        print(f"The word '{search_word}' appears {frequency} times in the file.")


# -----------------------------------------------------------------------------------


