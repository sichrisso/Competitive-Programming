class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0

        while i < len(nums):
            index = nums[i]-1
            if nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])

        return res