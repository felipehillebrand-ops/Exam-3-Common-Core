def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [e[::-1] for e in matrix]


print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))       # [[3, 2, 1], [6, 5, 4]]
print(mirror_matrix([[1, 2], [3, 4], [5, 6]]))      # [[2, 1], [4, 3], [6, 5]]
print(mirror_matrix([[7]]))                          # [[7]]
print(mirror_matrix([[1, 2, 3, 4]]))                 # [[4, 3, 2, 1]]
print(mirror_matrix([[-1, -2], [-3, -4]]))           # [[-2, -1], [-4, -3]]
