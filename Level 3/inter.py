def inter(s1: str, s2: str) -> str:
    res = ""

    for char in s1:
        if char in s2 and char not in res:
            res += char

    return res


print(inter("hello", "world"))  # "lo"
print(inter("banana", "band"))  # "ban"
print(inter("abcabc", "bc"))    # "bc"
