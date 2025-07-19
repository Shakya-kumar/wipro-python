# -----------------------------------------------------------------------------------
# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.
# -----------------------------------------------------------------------------------

t = (10, 20, 30, 40, 50, 60, 70)
print("4th element from first:", t[3])
print("4th element from last:", t[-4])


# -----------------------------------------------------------------------------------
# 2. Write a program to check whether an element exists in a tuple or not.
# -----------------------------------------------------------------------------------

t = (1, 2, 3, 4, 5)
element = int(input("Enter element to check: "))

if element in t:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")


# -----------------------------------------------------------------------------------
# 3. Write a program to convert a list into a tuple.
# -----------------------------------------------------------------------------------

lst = [10, 20, 30, 40]
converted_tuple = tuple(lst)
print("Converted tuple:", converted_tuple)


# -----------------------------------------------------------------------------------
# 4. Write a program to find the index of an item in a tuple.
# -----------------------------------------------------------------------------------

t = ('apple', 'banana', 'cherry', 'date')
item = input("Enter item to find index: ")

if item in t:
    index = t.index(item)
    print(f"Index of '{item}':", index)
else:
    print("Item not found in the tuple.")


# -----------------------------------------------------------------------------------
# 5. Write a program to replace the last value of tuples in a list to 100.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
# -----------------------------------------------------------------------------------

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in sample_list]
print("Updated list of tuples:", updated_list)
