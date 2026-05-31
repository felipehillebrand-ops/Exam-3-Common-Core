"""
Assignment name  : py_twist_sequence
Expected files   : py_twist_sequence.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that rotates an array to the right by k positions.
Rotating right by k means the last k elements move to the front.

def twist_sequence(arr: list[int], k: int) -> list[int]:

Input:  twist_sequence([1,2,3,4,5], 2)
Output: [4,5,1,2,3]

Input:  twist_sequence([1,2,3], 1)
Output: [3,1,2]

Input:  twist_sequence([1,2,3,4], 0)
Output: [1,2,3,4]

Input:  twist_sequence([1,2,3], 5)
Output: [3,2,1]

Input:  twist_sequence([], 3)
Output: []
"""


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
