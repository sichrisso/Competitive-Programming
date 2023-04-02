class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        output = {}
        double_nums = nums * 2
        for i in range(len(double_nums)):
            while stack and double_nums[i] > double_nums[stack[-1]]:
                pos = stack.pop()
                output[pos] = double_nums[i]
            stack.append(i)
        for i in range(len(nums)):
            if i in output:
                nums[i] = output[i]
            elif nums[i] == nums[stack[0]]:
                nums[i] = -1
            else:
                nums[i] = nums[stack[0]]
        return nums