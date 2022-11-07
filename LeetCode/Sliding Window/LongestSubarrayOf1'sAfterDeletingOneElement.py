def longestSubarray(self, nums: List[int]) -> int:
    dict = {}
    left, right, output = 0, 0, 0
    while right < len(nums):
        if nums[right] == 0 and nums[right] not in dict:
            dict[0] = right
        elif nums[right] == 0 and nums[right] in dict:
            left = dict[nums[right]] + 1
            dict[nums[right]] = right
        output = max(output, right - left + 1)
        right += 1
    return output - 1