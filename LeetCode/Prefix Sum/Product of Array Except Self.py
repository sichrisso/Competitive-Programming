class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        prefix = postfix = [1]
        output = []
        while left < len(nums) and right >= 0 :
            prefix.append(prefix[-1] * nums[left])
            postfix = [postfix[0] * nums[right]] + postfix 
            left += 1
            right -= 1
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i+1])
        return output
            