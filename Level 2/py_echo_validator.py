def echo_validator(text: str) -> bool:
    if text == "":
        return False
    new_text = "".join(c.lower() for c in text if c.isalpha())
    return new_text == new_text[::-1]


print(echo_validator("racecar"))
print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("race a car"))
print(echo_validator("Was it a car or a cat I saw"))
print(echo_validator("hello"))
print(echo_validator("Madam I'm Adam"))
print(echo_validator(""))
