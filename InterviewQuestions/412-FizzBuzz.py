#!/usr/bin/python3
"""
Given an integer n, return a string array answer (1-indexed) where:
- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.
"""

opening_message = """Hello, this is the FizzBuzz game.
For Instructions type I.

Please type a number:
"""

"""
def fizzBuzz(self, n):
    for x in range(n):
        if ((x % 5) == 0 and (x % 3) == 0):
            x = "FizzBuzz"
        if (x % 5) == 0:
            x = "Buzz"
        if (x % 5) == 0:
            x = "Fizz"

    return x
"""

def main(*args):
    print(opening_message)
    input = args

    print(argv)
    print(input)
