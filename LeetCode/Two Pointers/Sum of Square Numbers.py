class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        index = 0
        for i in range(c+1):
            if i**2 <= c:
                index = i
            else:
                break

        left, right = 0, index
        while left <= right:
            if left**2 + right**2 < c:
                left += 1
            elif left**2 + right**2 > c:
                right -= 1
            else:
                return True
        return False
          
   