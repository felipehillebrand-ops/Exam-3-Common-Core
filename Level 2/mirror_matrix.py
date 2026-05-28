def reverseMatrix(s):
    return [e[::-1] for e in s]


input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
print(reverseMatrix(input))
