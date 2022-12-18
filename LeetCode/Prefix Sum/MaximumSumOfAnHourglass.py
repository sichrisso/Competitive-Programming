def maxSum(self, grid: List[List[int]]) -> int:
      row = len(grid)
      column = len(grid[0])
      maxSum = 0
      for i in range(row - 2):
          for j in range(column - 2):
              upper = grid[i][j] + grid[i][j+1] + grid[i][j+2]
              middle = grid[i+1][j+1]
              lower = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
              sum = upper + middle + lower
              maxSum = max(maxSum, sum)
      return maxSum
