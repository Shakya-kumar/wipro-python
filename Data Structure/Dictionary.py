# -----------------------------------------------------------------------------------
# 1. Write a program to add a key and value to a dictionary.
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}
# -----------------------------------------------------------------------------------

sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("Updated Dictionary:", sample_dict)


# -----------------------------------------------------------------------------------
# 2. Write a program to concatenate the following dictionaries to create a new one.
# dic1 = {1:10, 2:20}, dic2 = {3:30, 4:40}, dic3 = {5:50, 6:60}
# Expected Result: {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# -----------------------------------------------------------------------------------

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {}
merged_dict.update(dic1)
merged_dict.update(dic2)
merged_dict.update(dic3)
print("Concatenated Dictionary:", merged_dict)


# -----------------------------------------------------------------------------------
# 3. Write a program to check if a given key already exists in a dictionary.
# -----------------------------------------------------------------------------------

my_dict = {1: "a", 2: "b", 3: "c"}
key_to_check = int(input("Enter key to check: "))

if key_to_check in my_dict:
    print("Key exists.")
else:
    print("Key does not exist.")


# -----------------------------------------------------------------------------------
# 4. Write a program to iterate over a dictionary using for loop and print:
# - Keys alone
# - Values alone
# - Both keys and values
# -----------------------------------------------------------------------------------

data = {"apple": 1, "banana": 2, "cherry": 3}

print("\nKeys:")
for key in data:
    print(key)

print("\nValues:")
for value in data.values():
    print(value)

print("\nKeys and Values:")
for key, value in data.items():
    print(f"{key}: {value}")


# -----------------------------------------------------------------------------------
# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are the square of the keys.
# -----------------------------------------------------------------------------------

squares = {}
for i in range(1, 16):
    squares[i] = i ** 2
print("\nDictionary of squares from 1 to 15:", squares)


# -----------------------------------------------------------------------------------
# 6. Write a program to sum all the values in a dictionary, assuming all values are integers.
# -----------------------------------------------------------------------------------

value_dict = {"x": 10, "y": 20, "z": 30}
total = sum(value_dict.values())
print("\nSum of all values:", total)
