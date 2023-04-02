class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      dict = Counter(nums)
      for i in range(1, len(nums)+1):
        if i not in dict:
          missed = i
        if dict[i] > 1:
          duplicate = i
      return [duplicate, missed]