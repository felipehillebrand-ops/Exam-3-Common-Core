"""
Assignment name: py_string_sculptor
Expected files: py_string_sculptor.py
Allowed functions: None

Write a function that transforms a string by alternating the case of alphabetic characters only. Non-alphabetic characters remain unchanged and are ignored for the purpose of alternation. The first alphabetic character should be lowercase, the second uppercase, the third lowercase, and so on.

Your function must be declared as follows:
def string_sculptor(text: str) -> str:

Examples:

Input:  string_sculptor("hello")
Output: "hElLo"

Input:  string_sculptor("Hello World")
Output: "hElLo wOrLd"

Input:  string_sculptor("abc123def")
Output: "aBc123DeF"

Input:  string_sculptor("Python3.9!")
Output: "pYtHoN3.9!"

Input:  string_sculptor("")
Output: ""
"""


def string_sculptor(text: str) -> str:
    s = ""
    i = 0
    p = True

    while i < len(text):
        if text[i].isalpha():
            if p:
                s += text[i].lower()
            else:
                s += text[i].upper()
            p = not p
        else:
            s += text[i]
            if text[i] == ' ':
                p = True
        i += 1
    return s


print(string_sculptor("hello"))
print(string_sculptor("Hello World"))
print(string_sculptor("abc123def"))
print(string_sculptor("Python3.9!"))
print(string_sculptor(""))
