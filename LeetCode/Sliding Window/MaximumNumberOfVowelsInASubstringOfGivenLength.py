def maxVowels(self, s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    l, r, v, output= 0, 0, 0, 0 
    while r < len(s):
        if r - l + 1 <= k:
            if s[r] in vowels:
                v += 1
            else:
                pass
            r += 1
        else:
            if s[r] in vowels:
                v += 1
            if s[l] in vowels:
                v -= 1
            l += 1
            r += 1
        output = max(output, v)
    return output
        
                