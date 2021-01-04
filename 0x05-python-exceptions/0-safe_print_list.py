#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    while (count < x):
        try:
            print("{}".format(my_list[count]), end="")
        except IndexError:
            print()
            return count
        count += 1

    print()
    return count
