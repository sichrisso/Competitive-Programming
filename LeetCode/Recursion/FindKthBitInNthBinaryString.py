def findKthBit(self, n: int, k: int) -> str:
    if n == 1:
        return "0"

    l = 2 ** n - 1
    
    mid = l // 2 + 1
    if k == mid:
        return "1"
    elif k < mid:
        return self.findKthBit(n - 1, k)
    else:
        return str(1 - int(self.findKthBit(n - 1, l - k + 1)))