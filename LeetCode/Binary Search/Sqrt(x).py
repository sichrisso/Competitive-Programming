class Solution:
    def mySqrt(self, x: int) -> int:
        mid, l, r = 0, 1, x
        if x == 0:
            return x
        while l <= r and (l + r)//2 != mid:
            mid = (l + r)//2
            num = mid * mid
            if num < x:
                l = mid
            elif num > x:
                r = mid 
            else:
                return mid
        return l

       