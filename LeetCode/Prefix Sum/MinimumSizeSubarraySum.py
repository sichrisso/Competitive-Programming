def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    prefix = [0]
    l, r, output = 0, 0, 0
    for i in range(len(nums)):
        prefix.append(prefix[-1] + nums[i])
    while l < len(prefix):
        if prefix[r] - prefix[l] < target:
            if r < len(prefix) - 1:
                r += 1
            else:
                l += 1
        elif prefix[r] - prefix[l] >= target:
            if output == 0:
                output = r - l
            else:
                output = min(output, r - l)
            l += 1
    return output