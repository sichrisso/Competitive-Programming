class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def predict(left, right):
            if left == right:
                return nums[left]
            return max(nums[left] - predict(left+1, right), nums[right] - predict(left, right-1))
        score = predict(0, len(nums)-1)
        return score >= 0