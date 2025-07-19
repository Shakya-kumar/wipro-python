# -----------------------------------------------------------------------------------
# 1. Write a program to remove a given item from the set.
# -----------------------------------------------------------------------------------

my_set = {10, 20, 30, 40, 50}
item = int(input("Enter the item to remove from set: "))

if item in my_set:
    my_set.remove(item)
    print("Updated set after removal:", my_set)
else:
    print("Item not found in the set.")


# -----------------------------------------------------------------------------------
# 2. Write a program to create an intersection of sets.
# -----------------------------------------------------------------------------------

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1.intersection(set2)
print("Intersection of sets:", intersection)


# -----------------------------------------------------------------------------------
# 3. Write a program to create a union of sets.
# -----------------------------------------------------------------------------------

set1 = {1, 2, 3}
set2 = {4, 5, 6}

union = set1.union(set2)
print("Union of sets:", union)


# -----------------------------------------------------------------------------------
# 4. Write a program to find the maximum and minimum value in a set.
# -----------------------------------------------------------------------------------

numbers = {23, 89, 15, 42, 77}

maximum = max(numbers)
minimum = min(numbers)

print("Maximum value in the set:", maximum)
print("Minimum value in the set:", minimum)
