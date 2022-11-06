def largestNumber(self, nums: List[int]) -> str:
        for i in range (len(nums)):
            nums[i] = str(nums[i])
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if int(nums[i] + nums[j]) > int(nums[j] + nums[i]):
                    pass
                else:
                    nums[i],nums[j] = nums[j], nums[i]
        return str(int("".join(nums)))