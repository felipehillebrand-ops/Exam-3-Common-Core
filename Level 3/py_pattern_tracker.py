"""
Assignment name  : py_pattern_tracker
Expected files   : py_pattern_tracker.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that counts the number of valid consecutive digit pairs in a
string. A valid pair consists of two adjacent digits where the second digit
is exactly one greater than the first digit. A 9 followed by a 0 is NOT a valid pair

Your function must be declared as follows:

def pattern_tracker(text: str) -> int:

Examples:

Input: pattern_tracker("123")
Output: 2

Input: pattern_tracker("12a34")
Output: 2

Input: pattern_tracker("987654321")
Output: 0

Input: pattern_tracker("01234567")
Output: 7

Input: pattern_tracker("abc")
Output: 0

Input: pattern_tracker("1a2b3c4")
Output: 0

Input: pattern_tracker("112233")
Output: 2
"""


def pattern_tracker(text: str) -> int:
    count = 0

    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit() and text[i + 1] > text[i]:
            count += 1
    return count


print(pattern_tracker("123"))
print(pattern_tracker("12a34"))
print(pattern_tracker("987654321"))
print(pattern_tracker("01234567"))
print(pattern_tracker("abc"))
print(pattern_tracker("1a2b3c4"))
print(pattern_tracker("112233"))
