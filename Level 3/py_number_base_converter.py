"""
Assignment name  : py_number_base_converter
Expected files   : py_number_base_converter.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that converts a number from one base to another.
Support bases from 2 to 36 inclusive, using digits 0-9 and letters A-Z for values 10-35. Return "ERROR" for invalid inputs (base, digits)

Your function must be declared as follows:

def number_base_converter(number: str, from_base: int, to_base: int) -> str:

Examples:

Input: number_base_converter("1010", 2, 10)
Output: "10"

Input: number_base_converter("FF", 16, 10)
Output: "255"

Input: number_base_converter("255", 10, 16)
Output: "FF"

Input: number_base_converter("123", 10, 2)
Output: "1111011"

Input: number_base_converter("Z", 36, 10)
Output: "35"

Input: number_base_converter("35", 10, 36)
Output: "Z"

Input: number_base_converter("123", 1, 10)
Output: "ERROR"

Input: number_base_converter("G", 16, 10)
Output: "ERROR"
"""


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    base_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    try:
        if not 2 <= from_base <= 36:
            return "ERROR"
        if not 2 <= to_base <= 36:
            return "ERROR"

        n = int(number, from_base)
        if n == 0:
            return "0"

        res = ""
        while n > 0:
            res = base_str[n % to_base] + res
            n //= to_base
        return res

    except Exception:
        return "ERROR"


print(number_base_converter("1010", 2, 10))
print(number_base_converter("FF", 16, 10))
print(number_base_converter("255", 10, 16))
print(number_base_converter("123", 10, 2))
print(number_base_converter("Z", 36, 10))
print(number_base_converter("35", 10, 36))
print(number_base_converter("123", 1, 10))
print(number_base_converter("G", 16, 10))
