class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curr = 0, 0
        ans = float(inf)
        for i in range(len(nums)):
            curr+=nums[i]
            while curr >= target:
                ans=min(ans,i-l+1) 
                curr-=nums[l] 
                l+=1
        return 0 if ans == float(inf) else ans
        