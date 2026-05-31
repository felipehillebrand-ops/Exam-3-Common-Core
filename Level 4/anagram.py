"""
Verifica se duas strings são anagramas (se contêm exatamente as mesmas letras),
com a mesma quantidade, independentemente de maiúsculas/minúsculas e espaços.
"""


def Anagram(s1: str, s2: str) -> bool:
    new_s1 = s1.upper().replace(" ", "")
    new_s2 = s2.upper().replace(" ", "")

    if len(new_s1) != len(new_s2):
        return False

    return sorted(new_s1) == sorted(new_s2)


print(Anagram("listen", "silent")) # True
print(Anagram("Triangle", "Integral")) # True
print(Anagram("Dormitory", "Dirty Room")) # True
print(Anagram("Astronomer", "Moon starer")) # True
print(Anagram("hello", "world")) # False
print(Anagram("test", "ttew")) # False
print(Anagram("abc", "abcc")) # False
print(Anagram("", "")) # True
print(Anagram("a gentleman", "elegant man")) # True
print(Anagram("aabb", "ab")) # False
