class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        def subarray(index, hold):
            if len(self.output) == 2**len(nums):
                return
            if len(hold) <= len(nums):
                self.output.append(hold.copy())
            for i in range(index, len(nums)):
                hold.append(nums[i])
                subarray(i+1, hold)
                hold.pop()
        subarray(0, [])
        return self.output

        
           