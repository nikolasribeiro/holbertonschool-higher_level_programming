#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    def print_format(operator, first, second, calc):
        print("{} {} {} = {}".format(first, operator, second, calc(first, second)))

    a = 10
    b = 5
    print_format(operator="+", first=a, second=b, calc=add)
    print_format(operator="-", first=a, second=b, calc=sub)
    print_format(operator="*", first=a, second=b, calc=mul)
    print_format(operator="/", first=a, second=b, calc=div)
