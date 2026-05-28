def pattern_tracker(text: str) -> int:
    count = 0

    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit() and text[i + 1] > text[i]:
            count += 1
    return count


print(pattern_tracker("123"))
print(pattern_tracker("12a34"))
print(pattern_tracker("987654321"))
print(pattern_tracker("01234567"))
print(pattern_tracker("abc"))
print(pattern_tracker("1a2b3c4"))
print(pattern_tracker("112233"))
