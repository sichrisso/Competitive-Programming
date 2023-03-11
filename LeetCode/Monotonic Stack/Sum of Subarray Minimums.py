class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        left = []
        right = []
        ans = arr.copy()

        while l < len(arr) and r > -1:
            ind = l
            while left and left[-1][1] >= arr[l]:
                ind, _ = left.pop()
            ans[l] *= (l-ind+1)
            left.append((ind, arr[l]))
            l += 1
            ind = r
            while right and right[-1][1] > arr[r]:
                ind, _ = right.pop()
            ans[r] *= (ind-r+1)
            right.append((ind, arr[r]))
            r -= 1
        return sum(ans) % (10**9+7)