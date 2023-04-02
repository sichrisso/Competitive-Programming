class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(start, prev):
            if start == len(s):
                return True
            for i in range(start, len(s)):
                val = int(s[start:i+1])
                if val + 1 == prev and dfs(i+1, val):
                    return True
            return False
           
        for i in range(len(s) - 1):
            prev = int(s[:i+1])
            if dfs(i+1, prev): return True
        return False


       
    