# def string_permutation_checker(s1: str, s2:str) -> bool

# write a function that determines if two strings are permutation of each other. Two strings are permutation of each other if they contain the same characters with the same frequencies .

# Check if both strings contain the same characters 
# Count the character frequencies (case sensitive)
# return True if they are permutations and False otherwise
# Handle empty strings (they are permutations)
# Consider whitespaces and punctions as regular charactares


def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


print(string_permutation_checker("abc", "Bca"))
print(string_permutation_checker("abc", "def"))
print(string_permutation_checker("", ""))
print(string_permutation_checker("a", ""))
print(string_permutation_checker("a", "a"))
print(string_permutation_checker("Test", "tste"))
