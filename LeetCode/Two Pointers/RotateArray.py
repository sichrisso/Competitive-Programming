def rotate(self, nums: List[int], k: int) -> None:
    if len(nums) == 2:
        while k > 0:
            nums[0], nums[1] = nums[1], nums[0]
            k -= 1
    else:
        nums[:len(nums) - k] = reversed(nums[:len(nums) - k])
        nums[len(nums) - k:] = reversed(nums[len(nums) - k:])
        nums[:len(nums)] = reversed(nums[:len(nums)])