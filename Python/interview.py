#!/usr/bin/env python3
"""
Contains the class TestConsoleDocs
"""
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tuplee = (1, 2, 3, 4, 5, 6, 7, 8, 9)

dictionary = {
    "Name": "Chris",
    "Age": 25,
    "Got_the_job": True,
}

def saludar_amigos():
    """for x in range(len(array)):
        print(x, "hola amigos")

    for x in iter(tuplee):
        print(x, "hola amigos")"""
    for x in dictionary.keys():
        print(x)


if __name__ == '__main__':
    saludar_amigos()
