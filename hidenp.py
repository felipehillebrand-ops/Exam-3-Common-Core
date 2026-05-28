def hidenp(small, big):
    it = iter(big)
    return all(c in it for c in small)


print(hidenp("abc", "a1b2c3"))   # True
print(hidenp("ace", "abcde"))    # True
print(hidenp("aec", "abcde"))    # False
print(hidenp("", "abc"))   # True
print(hidenp("", ""))      # True
print(hidenp("abc", "ab"))       # False
print(hidenp("xyz", "abc"))      # False
print(hidenp("aaaa", "aaa"))     # False
print(hidenp("aab", "aaab"))     # True
print(hidenp("aab", "ab"))       # False
print(hidenp("aba", "aabb"))     # True
print(hidenp("abc", "ABC"))      # False
print(hidenp("Abc", "Axxbxxc"))  # True
print(hidenp("sing", "subsequence testing"))   # True
print(hidenp("test", "tXeYzst"))               # True
print(hidenp("python", "ptyhon"))              # False
