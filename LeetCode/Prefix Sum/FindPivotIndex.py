def pivotIndex(self, nums: List[int]) -> int:
    right = 0
    left = 0
    x = 0
    y = 0
    for i in range(1, len(nums)):
        right += nums[i]
    while x < len(nums)-1:
        if left == right:
            break
        else:
            left += nums[x]
            x += 1
            right -= nums[x]

    if(left != right):
        return -1
    return x