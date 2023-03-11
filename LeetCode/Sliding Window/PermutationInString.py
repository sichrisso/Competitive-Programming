class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        countS1 = Counter(s1)
        for i in range(len(s2)):
            if s2[i] in s1 and r-l+1 <= len(s1):
                r += 1
            else:
                r += 1
                l += 1
            if Counter(s2[l:r]) == countS1:
                return True
        return False