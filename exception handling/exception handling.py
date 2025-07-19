

# 1. Write a program to accept two numbers from the user and perform division.
#    If any exception occurs, print an error message or else print the result.
def divide_numbers():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print("Unexpected error:", e)


# 2. Write a program to accept a number from the user and check whether it's prime or not.
#    If user enters anything other than number, handle the exception and print an error message.
def check_prime():
    try:
        num = int(input("Enter a number to check for prime: "))
        if num <= 1:
            print("Not a prime number.")
            return
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Not a prime number.")
                return
        print("It is a prime number.")
    except ValueError:
        print("Error: Please enter a valid integer.")


# 3. Write a program to accept the file name to be opened from the user.
#    If file exists, print the contents of the file in title case.
#    Else handle the exception and print an error message.
def read_file_title_case():
    try:
        filename = input("Enter the filename to open: ")
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content in Title Case:\n")
            print(content.title())
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected error:", e)


# 4. Declare a list with 10 integers and ask the user to enter an index.
#    Check whether the number in that index is positive or negative.
#    If any invalid index is entered, handle the exception and print an error message.
def check_list_index_value():
    numbers = [10, -5, 22, -1, 0, 3, -8, 7, -6, 14]
    try:
        index = int(input("Enter an index (0 to 9): "))
        value = numbers[index]
        if value > 0:
            print(f"The number at index {index} is Positive.")
        elif value < 0:
            print(f"The number at index {index} is Negative.")
        else:
            print(f"The number at index {index} is Zero.")
    except IndexError:
        print("Error: Invalid index. Please enter a number between 0 and 9.")
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print("Unexpected error:", e)


