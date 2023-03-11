class NumArray:

    def __init__(self, nums: List[int]):
        self.NumArray = nums
        for i in range(1, len(self.NumArray)):
            self.NumArray[i] += self.NumArray[i-1]
        
    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.NumArray[right]
        return self.NumArray[right] - self.NumArray[left-1]
       
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)