"""
Assignment name  : py_cryptic_sorter
Expected files   : py_cryptic_sorter.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that sorts a list of strings according to multiple criteria:

1. Primary sort: By string length (shortest first)
2. Secondary sort: Alphabetically (for strings of same length)
3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)

Your function must be declared as follows:

def cryptic_sorter(strings: list[str]) -> list[str]:

The function should return the sorted list.

Your function must handle:
- Empty strings and empty lists
- Mixed case strings (treat as lowercase for sorting)
- Special characters (ignore for vowel counting)

Examples:

Input: cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"])
Output: ["cat", "dog", "apple", "banana", "elephant"]

Input: cryptic_sorter(["aaa", "bbb", "AAA", "BBB"])
Output: ["AAA", "aaa", "BBB", "bbb"]

Input: cryptic_sorter(["hello", "world", "hi", "test"])
Output: ["hi", "test", "hello", "world"]

Input: cryptic_sorter([])
Output: []

Input: cryptic_sorter([""])
Output: [""]
"""


def cryptic_sorter(strings: list[str]) -> list[str]:
    vowels = set("aeiou")

    return sorted(strings, key=lambda s: (
        len(s),
        s.lower(),
        sum(1 for c in s.lower() if c in vowels),
        s
    ))


print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
print(cryptic_sorter(["hello", "world", "hi", "test"]))
print(cryptic_sorter([]))
print(cryptic_sorter([""]))

