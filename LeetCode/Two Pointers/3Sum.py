class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        for i in range(0, len(nums)-2):
            l = i + 1
            r = len(nums)-1
            while l < r:
                sumSoFar = nums[i] + nums[l] + nums[r]
                if sumSoFar > 0:
                    r -= 1
                elif sumSoFar < 0:
                    l += 1
                else:
                    output.append((nums[i], nums[l], nums[r]))
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return list(set(output))