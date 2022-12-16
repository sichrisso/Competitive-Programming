def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    row = len(matrix)
    column = len(matrix[0])
    transpose = [[0] * row for i in range(column)]
    for i in range(row):
        for j in range(column):
            transpose[j][i] = matrix[i][j] 
    return transpose   