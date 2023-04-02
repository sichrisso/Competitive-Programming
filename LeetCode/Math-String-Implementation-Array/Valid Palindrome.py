class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not i.isalnum():
                s= s.replace(i, '')
        s = s.lower()
        l = 0 
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
         
                