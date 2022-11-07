def isPowerOfFour(self, n: int) -> bool:
    x = 0
    result = 0
    while(result <= n):
        result = 4 ** x
        if result != n:
            x +=1
        elif result == n:
            return True 
        
    if result > n:
        return False