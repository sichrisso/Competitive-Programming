class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        output = set()
        def nonDecrease(index, hold):
            if len(hold) > 1:
                output.add(tuple(hold))
            for i in range(index, len(nums)):
                if len(hold) == 0 or nums[i] >= hold[-1]:
                    hold.append(nums[i])
                    nonDecrease(i+1, hold)
                    hold.pop()
            
        nonDecrease(0, [])
        return list(output)


   