def IsValidRomanNumber(value):
    thousand = "(?:(M){0,3})?"
    hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
    ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
    unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"

    regex_pattern = r"^" + thousand + hundred + ten + unit + "$"

    import re

    return bool(re.match(regex_pattern, value))


print((IsValidRomanNumber("XII")))

#Resource https://www.geeksforgeeks.org/validating-roman-numerals-using-regular-expression/