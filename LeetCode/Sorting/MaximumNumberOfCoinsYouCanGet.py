def maxCoins(self, piles: List[int]) -> int:
        output = 0
        piles.sort()
        while (len(piles) > 0):
            alice = piles.pop()
            bob = piles.pop(0)
            output += piles.pop()
        return output