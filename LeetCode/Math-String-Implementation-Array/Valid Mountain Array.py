class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        l, r = 0, n - 1
        if n < 3:
            return False

        while l < n - 2 and arr[l] < arr[l + 1]:
            l += 1
        
        while r > 1 and arr[r] < arr[r - 1]:
            r -= 1
        
        return l == r

    