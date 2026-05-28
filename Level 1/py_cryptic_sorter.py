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
