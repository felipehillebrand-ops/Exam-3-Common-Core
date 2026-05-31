"""
Assignment name  : py_echo_validator
Expected files   : py_echo_validator.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that checks if a string is a palindrome, ignoring spaces and case, only cons

Your function must be declared as follows:

def echo_validator(text: str) -> bool:

Examples:

Input: echo_validator("racecar")
Output: True

Input: echo_validator("A man a plan a canal Panama")
Output: True

Input: echo_validator("race a car")
Output: False

Input: echo_validator("Was it a car or a cat I saw")
Output: True

Input: echo_validator("hello")
Output: False

Input: echo_validator("Madam Im Adam")
Output: True

Input: echo_validator("")
Output: False
"""


def echo_validator(text: str) -> bool:
    if text == "":
        return False
    new_text = "".join(c.lower() for c in text if c.isalpha())
    return new_text == new_text[::-1]


print(echo_validator("racecar"))
print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("race a car"))
print(echo_validator("Was it a car or a cat I saw"))
print(echo_validator("hello"))
print(echo_validator("Madam I'm Adam"))
print(echo_validator(""))
