class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        currSum = sum(nums[l:r])
        maxSum = currSum/k
        
        while r < len(nums):
            currSum -= nums[l]
            currSum += nums[r]
            r += 1
            l += 1
            
            maxSum = max(maxSum, currSum/k)
        return maxSum


       
       
       
       
       
       