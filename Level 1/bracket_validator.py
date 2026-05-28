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


print(bracket_validator("([](fdsdfds){})"))
