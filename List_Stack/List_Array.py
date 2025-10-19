
# Description: This is implements a List Data Structure using Python's array module.
# It allows the user to insert, delete, search, and display numbers in the list.

# Objective: The objective of this program is to implement a simple Array-based List Data Structure in Python. 
# It demonstrates how to perform basic list operations such as Insert, Delete, Search, Traverse, and Exit. 
# This program helps students understand how arrays can be used to store and manage data, as well as how to manipulate them using simple operations.

# Reference: Basic array operations in Python (docs.python.org)

import array as arr

list = arr.array('i', [])

# Function of Program 

def insert_at_start():
    value = int(input("Enter number to insert at start: "))
    list.insert(0, value)
    print(f"{value} successfully inserted at start.")

def insert_at_end():
    value = int(input("Enter number to insert at end: "))
    list.append(value)
    print(f"{value} successfully inserted at end.")

def insert_at_position():
    value = int(input("Enter number to insert: "))
    position = int(input("Enter position: "))
    if position < 0 or position > len(list):
        print("Error: Invalid position.")
    else:
        list.insert(position, value)
        print(f"{value} successfully inserted at position {position}.")

def delete_at_start():
    if len(list) == 0:
        print("Error: List is empty.")
    else:
        first_value = list[0]
        list.remove(first_value)
        print(first_value, "has been deleted from start.")

def delete_at_end():
    if len(list) == 0:
        print("Error: List is empty.")
    else:
        last_value = list[len(list)-1]
        list.remove(last_value)
        print(last_value, "has been deleted from end.")

def delete_at_position():
    position = int(input("Enter position to delete: "))
    if position < 0 or position >= len(list):
        print("Error: Invalid position.")
    else:
        value = list[position]
        list.remove(value)
        print(value, "has been deleted from position", position)


def delete_number():
    value = int(input("Enter number to delete: "))
    if value in list:
        list.remove(value)
        print(f"{value} has been successfully deleted.")
    else:
        print(f"{value} is not in the list and cannot be deleted.")

def search_number():
    value = int(input("Enter number to search: "))
    found = False
    count = 0
    for item in list:
        if item == value:
            print("Value", value, "is found at position", count)
            found = True
            break
        count += 1
    if not found:
        print("Value", value, "is not in the list")

def display_number_at_position():
    position = int(input("Enter position to display: "))
    if position < 0 or position >= len(list):
        print("Error: Invalid position.")
    else:
        print("Number at position of", position, "is", list[position])

def display_list():
    if len(list) == 0:
        print("List is empty.")
    else:
        print("\nCurrent List: ", end="")
        for value in list:
            print(value, end=" ")
        print()


print("\n---------------------------------------------------")
print("          Welcome To Array Operation System         ")
print("---------------------------------------------------")

# Main loop

while True:
    print("\n====== Array Operation System ======")
    print("[0] Exit")
    print("[1] Insert At Start")
    print("[2] Insert At End")
    print("[3] Insert At Position")
    print("[4] Delete At Start")
    print("[5] Delete At End")
    print("[6] Delete At Position")
    print("[7] Delete Number")
    print("[8] Search Number")
    print("[9] Display Number At Position")
    print("[10] Display List")
    print("====================================")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print(" Invalid input. Please enter a number.")
        continue

    if choice == 0:
        confirm = input("Are you sure you want to exit? (y/n): ")
        if confirm.lower() == 'y':
            print("Thank you for using Array Operation System!\n")
            break
    elif choice == 1:
        insert_at_start()
    elif choice == 2:
        insert_at_end()
    elif choice == 3:
        insert_at_position()
    elif choice == 4:
        delete_at_start()
    elif choice == 5:
        delete_at_end()
    elif choice == 6:
        delete_at_position()
    elif choice == 7:
        delete_number()
    elif choice == 8:
        search_number()
    elif choice == 9:
        display_number_at_position()
    elif choice == 10:
        display_list()
    else:
        print(" Invalid choice. Please try again.")


# Conclusion:
# This program successfully demonstrates the use of Array as a List Data Structure.
# It provides clear examples of how basic operations like insertion, deleting, searching, and traversal can be implemented in Python. 
# #The program is simple, easy to understand, and useful for beginners who want to learn about list operations and data structures.