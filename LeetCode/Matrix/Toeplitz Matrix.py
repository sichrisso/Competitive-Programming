class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def is_Toplitz(row, col):
            val = matrix[row][col]
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != val:
                    return False
                row += 1
                col += 1
            return True

        for col in range(len(matrix[0])):
            if not is_Toplitz(0, col):
                return False
        for row in range(1, len(matrix)):
            if not is_Toplitz(row, 0):
                return False
        return True
        
                    
         
                