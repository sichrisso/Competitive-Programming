class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        while l <= r:
            mid = (l+r)//2 
            less, great = 0, 0
            for i in range(len(nums)):
                if nums[i] < mid:
                    less += 1
                elif nums[i] > mid:
                    great += 1
            if  less + great < len(nums) - 1:
                return mid
            if less > mid - 1:
                r = mid - 1
            else:
                l = mid + 1 

            

            
        