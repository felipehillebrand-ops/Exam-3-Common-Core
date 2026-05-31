"""
Assignment name  : py_shadow_merge
Expected files   : py_shadow_merge.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that merges two sorted lists into one sorted list.

Your function must be declared as follows:

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:

Examples:

Input:  shadow_merge([1, 3, 5], [2, 4, 6])
Output: [1, 2, 3, 4, 5, 6]

Input:  shadow_merge([1, 2, 3], [4, 5, 6])
Output: [1, 2, 3, 4, 5, 6]

Input:  shadow_merge([1], [2, 3, 4])
Output: [1, 2, 3, 4]

Input:  shadow_merge([], [1, 2, 3])
Output: [1, 2, 3]

Input:  shadow_merge([1, 1, 2], [1, 3, 3])
Output: [1, 1, 1, 2, 3, 3]
"""


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    list1.extend(list2)
    list1.sort()
    return list1


print(shadow_merge([1, 3, 5], [2, 4, 6]))
print(shadow_merge([1, 2, 3], [4, 5, 6]))
print(shadow_merge([1], [2, 3, 4]))
print(shadow_merge([], [1, 2, 3]))
print(shadow_merge([1, 1, 2], [1, 3, 3]))
