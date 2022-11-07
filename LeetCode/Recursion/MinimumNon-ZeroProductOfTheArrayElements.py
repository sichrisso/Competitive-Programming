def minNonZeroProduct(self, p: int) -> int:
    MOD = 10 ** 9 + 7
    top = pow(2, p, MOD) - 1
    mid = top - 1
    midcount = pow(2, p-1)-1
    return (pow(mid, midcount, MOD) * top) % MOD