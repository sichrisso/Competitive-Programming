def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = 0
        left = 0
        total = 0
        output = 0
        while right < len(nums) and left < len(nums):
            total += nums[right]
            if (((nums[right]) * ((right - left) + 1)) <= (total + k)):
                dif = ((total + k) - ((nums[right]) * ((right - left) + 1)))
                output = max(output, ((right - left) + 1))
            elif (((nums[right]) * ((right - left) + 1)) > (total + k)):
                total -= nums[left]
                total -= nums[right]
                left += 1 
                right -= 1  
            right += 1

        if dif > k:
            return 1
        else:
            return output 