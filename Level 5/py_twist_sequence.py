def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    k = k % len(arr)
    if k == 0:
        return list(arr)
    return arr[-k:] + arr[:-k]


print(twist_sequence([1, 2, 3, 4, 5], 2))
print(twist_sequence([1, 2, 3], 1))
print(twist_sequence([1, 2, 3, 4], 0))
print(twist_sequence([1, 2, 3], 5))
print(twist_sequence([], 3))
