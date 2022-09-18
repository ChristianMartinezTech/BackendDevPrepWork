#!/usr/bin/env python3
"""
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""


def palindrome(x):
    # Function that turns a number into a string, reverse it and compare to
    # its original input
    rev = str(x)[::-1]

    if rev[-1] == "-":  # Checking for negative numbers
        return False

    if int(rev) == x:
        return True
    return False


def main():
    response = palindrome(12345654321)
    print(response)


if __name__ == '__main__':
    main()
