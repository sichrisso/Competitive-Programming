class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        if r * c != row * col:
            return mat
       
        k = 0
        output = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(row):
            for j in range(col):
                output[k//c][k%c] = mat[i][j]
                k += 1
        return output
            