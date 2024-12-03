#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("No arguments.")
    elif num_args == 1:
        print("Number of argument: 1")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"Number of arguments: {num_args}")
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
