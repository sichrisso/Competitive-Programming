class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        arr = self.getRow(rowIndex-1)
        output = [1] * (rowIndex+1)
        l, r = 0, 1
        for i in range(1, len(output)-1):
            output[i] = arr[l] + arr[r]
            l+=1
            r+=1
        return output