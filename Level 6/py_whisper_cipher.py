"""
Assignment name: py_whisper_cipher
Expected files: py_whisper_cipher.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that creates a simple cipher by shifting letters in a string by a given amount. Non-alphabetic characters should remain unchanged.

Your function must be declared as follows:

def whisper_cipher(text: str, shift: int) -> str:

Examples:

Input:  whisper_cipher("hello", 3)
Output: "khoor"

Input:  whisper_cipher("Hello World!", 1)
Output: "Ifmmp Xpsme!"

Input:  whisper_cipher("xyz", 3)
Output: "abc"

Input:  whisper_cipher("ABC123def", 5)
Output: "FGH123ijk"

Input:  whisper_cipher("", 10)
Output: ""
"""


def whisper_cipher(text: str, shift: int) -> str:
    res = ""

    for c in text:
        if 'a' <= c <= 'z':
            res += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            res += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            res += c
    return res


print(whisper_cipher("hello", 3))
print(whisper_cipher("Hello World!", 1))
print(whisper_cipher("xyz", 3))
print(whisper_cipher("ABC123def", 5))
print(whisper_cipher("", 10))
print(whisper_cipher("abc", -3))
