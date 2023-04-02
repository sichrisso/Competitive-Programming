class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] > target:
                    break
                elif matrix[i][j] < target:
                    continue
                else:
                    return True
        return False