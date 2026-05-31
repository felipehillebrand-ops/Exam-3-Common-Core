def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [e[::-1] for e in matrix]


input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
print(mirror_matrix(input))
