# /usr/bin/env python3
"""Function that receives a string and return the repeated characher and its index"""


def repeaded_char(char):
    """This function returns the first repeated char"""
    new_str = "" # New string
    repeated = "" # Repeated char

    for i in char:
        if i in new_str:
            repeated = i
        else:
            new_str += i

    # No repetition check
    if repeated is "":
        repeat_position = -1
    else:
        repeat_position = char.find(repeated) + 1

    return repeated, repeat_position


def main():
    char = "bdacefghai"
    # char = "abc"
    index = repeaded_char(char)
    print(index)

if __name__ == '__main__':
    main()
