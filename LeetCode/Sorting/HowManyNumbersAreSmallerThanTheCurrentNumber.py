def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        Smaller = 0
        Count = []
        for i in range (len(nums)):
            for j in range (len(nums)):
                if nums[j] < nums[i]:
                    Smaller +=1
            Count.append(Smaller)
            Smaller = 0
        return Count