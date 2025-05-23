#!/usr/bin/env python3
# Author ID: Shazma Hussain - (167689223)


# Define the list
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    """ Appends a new item to the end of the list with the value (last item + 1). """
    # Append the next number in sequence to the list
    ordered_list.append(ordered_list[-1] + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    """ Removes all values found in items_to_remove list from ordered_list. """
    # Remove each item in items_to_remove from ordered_list if it exists
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    # Initial list
    print(my_list)

    # Add items to the list
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)

    # Print list after adding items
    print(my_list)

    # Remove items from the list
    remove_items_from_list(my_list, [1, 5, 6])

    # Print list after removing items
    print(my_list)
