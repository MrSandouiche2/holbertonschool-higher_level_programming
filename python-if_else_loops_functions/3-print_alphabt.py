#!/usr/bin/python3

for letters in range(97, 123):
    if letters == ord("q") or letters == ord("e"):
        continue
    print("{:c}".format(letters), end="")
