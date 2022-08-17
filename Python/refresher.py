#!/usr/bin/python3
# This to execute this file as a script


def input_taking():
    """Taking in the user input"""
    message = input("My name is: ")
    checking_input(message)


def checking_input(message):
    """Checking the user input is not a number"""
    if message.isnumeric():
        print("Letters only.")
        input_taking()

    print("Hello " + message + "!")


def main():
    input_taking()


if __name__ == '__main__':
    main()
