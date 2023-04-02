class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        output = [0]*(n + 1)
        for a, b in requests:
            output[a] += 1
            output[b + 1] -= 1
        for i in range(1, n):
            output[i] += output[i - 1]
        
        nums.sort()
        output.pop()
        output.sort()

        return sum(a*b for a, b in zip(nums, output)) % mod