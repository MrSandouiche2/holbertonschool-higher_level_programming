#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add  # Import the function add from add_0.py

    a = 1  # Assign 1 to variable a
    b = 2  # Assign 2 to variable b

    # Call the add function and print the result using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))
