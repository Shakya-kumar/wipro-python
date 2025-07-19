# 1. Create a list of 5 integers and display the list items. Access individual elements through index.

my_list = [10, 20, 30, 40, 50]
print("Complete list:", my_list)
print("First element:", my_list[0])
print("Third element:", my_list[2])
print("Last element:", my_list[-1])


# 2. Append a new item to the end of the list.

my_list.append(60)
print("\nList after appending 60:", my_list)


# 3. Reverse the order of the items in the list.

my_list.reverse()
print("\nList after reversing:", my_list)


# 4. Print the number of occurrences of a specified element in a list.

count_list = [1, 2, 3, 2, 4, 2, 5]
element = 2
count = count_list.count(element)
print(f"\nNumber of occurrences of {element}:", count)


# 5. Append the items of list1 to list2 in the front.

list1 = [100, 200, 300]
list2 = [10, 20, 30]
list2 = list1 + list2
print("\nList2 after prepending list1 items:", list2)


# 6. Insert a new item before the second element in an existing list.

items = ["apple", "banana", "cherry"]
items.insert(1, "orange")
print("\nList after inserting 'orange' before second element:", items)


# 7. Remove the item from a specified index in a list.

numbers = [1, 2, 3, 4, 5]
index_to_remove = 2
removed_item = numbers.pop(index_to_remove)
print(f"\nList after removing item at index {index_to_remove} ({removed_item}):", numbers)


# 8. Remove the first occurrence of a specified element from a list.

values = [7, 8, 9, 8, 10]
element_to_remove = 8
values.remove(element_to_remove)
print(f"\nList after removing first occurrence of {element_to_remove}:", values)
