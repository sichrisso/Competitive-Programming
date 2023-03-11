class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        Sum, output = 0, 0
        dict = {0:1}
        for i in range(len(nums)):
            Sum += nums[i]
            if (Sum % k) in dict:
                output += dict[Sum % k]
                dict[(Sum%k)] += 1
            else:
                dict[(Sum%k)] = 1
        return output 