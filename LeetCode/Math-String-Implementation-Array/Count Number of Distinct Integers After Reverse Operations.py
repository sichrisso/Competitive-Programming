class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            num = list(str(nums[i]))
            num.reverse()
            newNum = "".join(num)
            newNum = int(newNum)
            nums.append(newNum)
        return len(set(nums))