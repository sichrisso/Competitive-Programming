def moveZeroes(self, nums: List[int]) -> None:
    i = 0
    count = nums.count(0)
    zeros = [0] * count
    while i != len(nums):
        if nums[i] == 0:
            nums.remove(nums[i])
            i -= 1
        else:
            pass
        i += 1
    nums += zeros