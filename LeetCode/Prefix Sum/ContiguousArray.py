def findMaxLength(self, nums: List[int]) -> int:
    output, prefix = 0, -1
    dict = {-1:-1}
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1

    for i in range(len(nums)):
        prefix += nums[i]
        if prefix in dict:
            output = max(output, i- dict[prefix])
        else:
            dict[prefix] = i
    return output
