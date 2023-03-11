class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.NumMatrix = [[0] * (len(matrix[0]) + 1)]
        for i in range(len(matrix)):
            if i == 0:
                self.NumMatrix.append([0] + list(accumulate(matrix[i])))
                prev = [0] + list(accumulate(matrix[i]))
            else:
                x = [0] + list(accumulate(matrix[i]))
                prev = [sum(i) for i in list(zip(prev, x))]
                self.NumMatrix.append(prev)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        whole = self.NumMatrix[row2 + 1][col2 + 1] - self.NumMatrix[row2 + 1][col1]
        part = self.NumMatrix[row1][col2 + 1] - self.NumMatrix[row1][col1]
        return whole - part
      

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)