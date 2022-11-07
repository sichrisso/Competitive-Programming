def longestOnes(self, nums: List[int], k: int) -> int:
    right, left, total, output = 0, 0, 0, 0
    while right < len(nums) and left < len(nums):
        total += nums[right]
        if ((total + k) >= (1 * ((right - left) + 1))):
            output = max(output, (right-left)+1)
        else:
            total -= nums[left]
            left += 1    
        right += 1       
    return output 