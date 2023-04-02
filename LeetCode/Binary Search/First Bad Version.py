# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        version, l, r = 0, 1, n
      
        while l < r:
            version = (l + r)//2
            if isBadVersion(version):
                r = version  
            else:
                l = version + 1 
        return l


       