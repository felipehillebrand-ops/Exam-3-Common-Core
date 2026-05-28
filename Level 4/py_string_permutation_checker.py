def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


print(string_permutation_checker("abc", "Bca"))
print(string_permutation_checker("abc", "def"))
print(string_permutation_checker("", ""))
print(string_permutation_checker("a", ""))
print(string_permutation_checker("a", "a"))
print(string_permutation_checker("Test", "tste"))
