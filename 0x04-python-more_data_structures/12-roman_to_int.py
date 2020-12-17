#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num = 0

    for loop_variable in range(len(roman_string)):

        if roman_dict.get(roman_string[loop_variable], 0) == 0:
            return (0)

        if (loop_variable != (len(roman_string) - 1) and
                roman_dict[roman_string[loop_variable]] <
                roman_dict[roman_string[loop_variable + 1]]):
            num += roman_dict[roman_string[loop_variable]] * -1

        else:
            num += roman_dict[roman_string[loop_variable]]

    return (num)
