"""
Verifica se duas strings são anagramas (se contêm exatamente as mesmas letras),
com a mesma quantidade, independentemente de maiúsculas/minúsculas e espaços.
"""


def anagram(s1: str, s2: str) -> bool:
    new_s1 = s1.upper().replace(" ", "")
    new_s2 = s2.upper().replace(" ", "")

    if len(new_s1) != len(new_s2):
        return False

    return sorted(new_s1) == sorted(new_s2)


print(anagram("listen", "silent")) # True
print(anagram("Triangle", "Integral")) # True
print(anagram("Dormitory", "Dirty Room")) # True
print(anagram("Astronomer", "Moon starer")) # True
print(anagram("hello", "world")) # False
print(anagram("test", "ttew")) # False
print(anagram("abc", "abcc")) # False
print(anagram("", "")) # True
print(anagram("a gentleman", "elegant man")) # True
print(anagram("aabb", "ab")) # False
