def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    output = []
    columnStart, columnEnd = 0, len(matrix[0]) 
    rowStart, rowEnd = 0, len(matrix)
    while rowStart < rowEnd and columnStart < columnEnd:
        for i in range(columnStart, columnEnd):
            output.append(matrix[rowStart][i])
        rowStart += 1

        for i in range(rowStart, rowEnd):
            output.append(matrix[i][columnEnd-1])
        columnEnd -= 1

        if not (rowStart < rowEnd and columnStart < columnEnd): break

        for i in range(columnEnd-1, columnStart-1, -1):
            output.append(matrix[rowEnd-1][i])
        rowEnd -= 1

        for i in range(rowEnd-1, rowStart-1, -1):
            output.append(matrix[i][columnStart])
        columnStart += 1

    return output