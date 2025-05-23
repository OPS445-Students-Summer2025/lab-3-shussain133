#!/usr/bin/env python3
# '''Lab 3 Inv 2 function operate'''
# Author ID: Shazma Hussain - (167689223)


def operate(number1, number2, operator):
    if operator == "add":
        return number1 + number2
    elif operator == "subtract":
        return number1 - number2
    elif operator == "multiply":
        return number1 * number2
    else:
        # Change the quotes in the error message to double quotes as expected by the test
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    # Test cases for the operate function
    print(operate(10, 5, 'add'))        # Should return 15
    print(operate(10, 5, 'subtract'))   # Should return 5
    print(operate(10, 5, 'multiply'))   # Should return 50
    print(operate(10, 5, 'divide'))     # Should return the error message
