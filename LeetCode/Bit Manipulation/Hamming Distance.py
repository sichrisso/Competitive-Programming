class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        finalAns = bin(x ^ y)
        count = 0

        for i in range(2, len(finalAns)):
            if finalAns[i] == "1":
                count += 1
        return count

        