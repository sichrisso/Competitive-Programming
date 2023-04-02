class Solution:
    def findComplement(self, num: int) -> int:
        x = 1
        while x <= num:
            x = x << 1
        return (x-1) ^ num