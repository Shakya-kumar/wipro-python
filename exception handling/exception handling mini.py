# -----------------------------------------------------------------------------------
# Stream: Python
# Tech Module: Exception Handling
# Project: 1
#
# You had saved the items and their price details in a text file, which you purchased
# yesterday from a nearby super market.
#
# You need to know:
# 1. How many items did you purchase?
# 2. How many items are free?
# 3. What is the total amount you had to pay?
# 4. What is the discount amount?
# 5. What is the final amount did you pay after the discount?
#
# Help yourself by writing a python code to do this. Include necessary code to handle
# the possible exceptions.
#
# Sample file content:
# Chocolate 50
# Biscuit 35
# Icecream 50
#
# Perfume Free
# Soup Free
#
# Discount 30
# -----------------------------------------------------------------------------------

def process_purchase_file():
    try:
        filename = input("Enter the file name: ")
        with open(filename, 'r') as file:
            purchased_count = 0
            free_count = 0
            total_amount = 0
            discount = 0
            reached_discount = False

            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split()

                if parts[0].lower() == "discount":
                    try:
                        discount = int(parts[1])
                        reached_discount = True
                    except (IndexError, ValueError):
                        continue

                elif not reached_discount:
                    try:
                        price = parts[1]
                        if price.lower() == 'free':
                            free_count += 1
                        else:
                            total_amount += int(price)
                            purchased_count += 1
                    except (IndexError, ValueError):
                        continue

        final_amount = total_amount - discount

        print("\nSummary:")
        print(f"No of items purchased: {purchased_count}")
        print(f"No of free items: {free_count}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

process_purchase_file()
