def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
    
        for i in range (len(nums)):
            if nums[i] == target:
                output.append(i)
            else:
                continue
        return output
