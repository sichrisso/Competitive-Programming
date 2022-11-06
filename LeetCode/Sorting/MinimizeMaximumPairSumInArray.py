def minPairSum(self, nums: List[int]) -> int:
        output = []
        nums.sort()
        x = len(nums)//2
        left = nums[:(len(nums)//2)]
        right = nums[(len(nums)//2):] 
        while(len(left) > 0 and len(right) > 0):
            sum = left.pop(0) + right.pop() 
            output.append(sum)
        return max(output)