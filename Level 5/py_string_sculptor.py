def string_sculptor(text: str) -> str:
    s = ""
    i = 0
    p = True

    while i < len(text):
        if text[i].isalpha():
            if p:
                s += text[i].lower()
            else:
                s += text[i].upper()
            p = not p
        else:
            s += text[i]
            if text[i] == ' ':
                p = True
        i += 1
    return s


print(string_sculptor("hello"))
print(string_sculptor("Hello World"))
print(string_sculptor("abc123def"))
print(string_sculptor("Python3.9!"))
print(string_sculptor(""))
