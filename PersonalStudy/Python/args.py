#!/usr/bin/python3

# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

def main():
    print("Inputy as many numbers as you would like to sum:")
    result = my_sum()
    print("Your result is:", result)

if __name__ == '__main__':
    main()
