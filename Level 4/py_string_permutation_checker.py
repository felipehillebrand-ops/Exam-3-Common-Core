"""
Assignment name  : py_string_permutation_checker
Expected files   : py_sstring_permutation_checker.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that determines if two strings are permutation of each other. 
Two strings are permutation of each other if they contain the same characters with the same frequencies.

- Check if both strings contain the same characters 
- Count the character frequencies (case sensitive)
- Return True if they are permutations and False otherwise
- Handle empty strings (they are permutations)
- Consider whitespaces and punctions as regular charactares

Your function must be declared as follows:

def string_permutation_checker(s1: str, s2: str) -> bool

Examples:

Input:  string_permutation_checker("abc", "bca"))
Output: True

Input:  string_permutation_checker("abc", "def"))
Output: False

Input:  string_permutation_checker("listen", "silent"))
Output: True

Input:  string_permutation_checker("hello", "bello"))
Output: False

Input:  string_permutation_checker("", ""))
Output: True

Input:  string_permutation_checker("a", ""))
Output: False

Input:  string_permutation_checker("Abc", "abc"))
Output: False

Input:  string_permutation_checker("a gentleman", "elegant man"))
Output: True
"""


def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


print(string_permutation_checker("abc", "bca"))                 # True
print(string_permutation_checker("abc", "def"))                 # False
print(string_permutation_checker("listen", "silent"))           # True
print(string_permutation_checker("hello", "bello"))             # False
print(string_permutation_checker("", ""))                       # True
print(string_permutation_checker("a", ""))                      # False
print(string_permutation_checker("Abc", "abc"))                 # False
print(string_permutation_checker("a gentleman", "elegant man")) # True
