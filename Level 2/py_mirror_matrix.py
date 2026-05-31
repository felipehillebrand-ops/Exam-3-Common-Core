"""
Assignment name  : py_mirror_matrix
Expected files   : py_mirror_matrix.py
Allowed functions: None
--------------------------------------------------------------------------------

Given a 2D matrix `s` (list of lists), return a new matrix where
the order of elements is completely reversed.

The function must:
    -> Reverse the entire matrix as if it were flattened.
    -> Preserve the original dimensions of the matrix.
    -> Return a new matrix with elements in reversed order.

Your function must be declared as follows:

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]

Examples:

Input: mirror_matrix([[1, 2, 3], [4, 5, 6]]))
Output: [[3, 2, 1], [6, 5, 4]]

Input: mirror_matrix([[1, 2], [3, 4], [5, 6]]))
Output: [[2, 1], [4, 3], [6, 5]]

Input: mirror_matrix([[7]]))
Output: [[7]]

Input: mirror_matrix([[1, 2, 3, 4]]))
Output: [[4, 3, 2, 1]]

Input: mirror_matrix([[-1, -2], [-3, -4]]))
Output: [[-2, -1], [-4, -3]]
"""


def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [e[::-1] for e in matrix]


print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))       # [[3, 2, 1], [6, 5, 4]]
print(mirror_matrix([[1, 2], [3, 4], [5, 6]]))      # [[2, 1], [4, 3], [6, 5]]
print(mirror_matrix([[7]]))                          # [[7]]
print(mirror_matrix([[1, 2, 3, 4]]))                 # [[4, 3, 2, 1]]
print(mirror_matrix([[-1, -2], [-3, -4]]))           # [[-2, -1], [-4, -3]]
