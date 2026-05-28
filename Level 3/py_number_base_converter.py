def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    base_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    try:
        if not 2 <= from_base <= 36:
            return "ERROR"
        if not 2 <= to_base <= 36:
            return "ERROR"

        n = int(number, from_base)
        if n == 0:
            return "0"

        res = ""
        while n > 0:
            res = base_str[n % to_base] + res
            n //= to_base
        return res

    except Exception:
        return "ERROR"


print(number_base_converter("1010", 2, 10))
print(number_base_converter("FF", 16, 10))
print(number_base_converter("255", 10, 16))
print(number_base_converter("123", 10, 2))
print(number_base_converter("Z", 36, 10))
print(number_base_converter("35", 10, 36))
print(number_base_converter("123", 1, 10))
print(number_base_converter("G", 16, 10))
