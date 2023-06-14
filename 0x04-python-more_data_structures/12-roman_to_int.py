#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    num, i = 0, len(roman_string) - 1
    while i >= 0:
        if roman_string[i] == 'I':
            if (i+1 < len(roman_string) and
               (roman_string[i+1] == 'V' or roman_string[i+1] == 'X')):
                num -= 1
            else:
                num += 1
        elif roman_string[i] == 'V':
            num += 5
        elif roman_string[i] == 'X':
            if (i+1 < len(roman_string) and
               (roman_string[i+1] == 'L' or roman_string[i+1] == 'C')):
                num -= 10
            else:
                num += 10
        elif roman_string[i] == 'L':
            num += 50
        elif roman_string[i] == 'C':
            if (i+1 < len(roman_string) and
               (roman_string[i+1] == 'D' or roman_string[i+1] == 'M')):
                num -= 100
            else:
                num += 100
        elif roman_string[i] == 'D':
            num += 500
        elif roman_string[i] == 'M':
            num += 1000
        i -= 1
    return num
