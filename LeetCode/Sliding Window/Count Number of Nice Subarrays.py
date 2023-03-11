class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = output = 0
        prefix = {0 : 1}
        
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                count += 1
            if count - k in prefix:
                output += prefix[count - k] 
            if count in prefix:
                prefix[count] += 1
            else:
                prefix[count] = 1
        return output