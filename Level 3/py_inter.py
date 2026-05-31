"""
Retorna uma string com os caracteres que aparecem em ambas as strings,
sem repetições.
Os caracteres são adicionados na ordem em que aparecem na primeira string.
"""


def inter(s1: str, s2: str) -> str:
    res = ""

    for char in s1:
        if char in s2 and char not in res:
            res += char

    return res


print(inter("hello", "world"))  # "lo"
print(inter("banana", "band"))  # "ban"
print(inter("abcabc", "bc"))    # "bc"
