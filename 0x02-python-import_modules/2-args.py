#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    def print_on_console(validator, count, formatter=""):
        if validator:
            print("{}: {}".format(count, formatter))
        else:
            print("{} argument. ".format(count))

    total_arguments = len(argv) - 1

    if total_arguments == 0:
        print_on_console(False, total_arguments)
    elif total_arguments == 1:
        print_on_console(False, total_arguments)
    else:
        print_on_console(False, total_arguments)
    for i in range(total_arguments):
        print_on_console(True, i+1, argv[i + 1])
