#!/usr/bin/python3
def print_format(operator, first, second, submodule):
    print("{} {} {} = {}".format(first, operator, second, submodule(first, second)))


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print_format(operator="+", first=a, second=b, submodule=add)
    print_format(operator="-", first=a, second=b, submodule=sub)
    print_format(operator="*", first=a, second=b, submodule=mul)
    print_format(operator="/", first=a, second=b, submodule=div)
