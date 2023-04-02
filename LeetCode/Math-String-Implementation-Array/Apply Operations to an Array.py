class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0
            left += 1
            right += 1
      
        zero, number = [], []
        for i in nums:
            if i == 0:
               zero.append(i)
            else:
                number.append(i)
        return number + zero