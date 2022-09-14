#!/usr/bin/python3

# Mutables
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Inmutables
tup_num = ("Holaaa", 2, 5.6, True)

print(type(list_num), list_num)
print(type(tup_num), tup_num)

# Slices start:stop:step
print(list_num[0:6:2])
print(list_num[2:8:2])
print(list_num[:-1])
print(list_num[-1:])
print(list_num[::-1])
