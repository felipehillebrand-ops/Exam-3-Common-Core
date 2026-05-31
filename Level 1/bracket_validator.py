Assignment name  : py_bracket_validator
Expected files   : py_bracket_validator.py
Allowed functions: None
--------------------------------------------------------------------------------
# Write a function that checks if the brackets in a string are valid.
# A string is valid if every opening bracket has a matching closing bracket
# in the correct order.
# Allowed brackets: (), [], {}

# def bracket_validator(s: str) -> bool:
#
# Input:  brackets("()")
# Output: True
#
# Input:  brackets("()[]{}")
# Output: True
#
# Input:  brackets("(]")
# Output: False
#
# Input:  brackets("([)]")
# Output: False
#
# Input:  brackets("{[]}")
# Output: True
#
# Input:  brackets("")
# Output: True


def bracket_validator(s: str) -> bool:
    left = ['(', '[', '{']
    right = [')', ']', '}']
    stack = []
    i = 0

    while i < len(s):
        if s[i] in left:
            stack.append(s[i])
        if s[i] in right:
            if not stack:
                return False
            t = stack.pop()
            if s[i] == ')' and t != '(':
                return False
            if s[i] == ']' and t != '[':
                return False
            if s[i] == '}' and t != '{':
                return False
        i += 1
    return len(stack) == 0


print(py_bracket_validator("()"))  # True
print(py_bracket_validator("()[]{}"))  # True
print(py_bracket_validator("(]"))  # False
print(py_bracket_validator("([)]"))  # False
print(py_bracket_validator("{[]}"))  # True
print(py_bracket_validator("hello(world)[test]{code}"))  # True
print(py_bracket_validator("((()))"))  # True
print(py_bracket_validator("((())"))  # False
print(py_bracket_validator(""))  # True
