class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = {}
        right, left, total, output = 0, 0, 0, 0
        while right < len(s) and left < len(s):
            if s[right] in dict:
                dict[s[right]] += 1
            else:
                dict[s[right]] = 1
            total = max(dict.values())
            if ((total + k) >= (1 * ((right - left) + 1))):
                output = max(output, (right-left)+1)
            else:
                dict[s[left]] -= 1
                left += 1    
            right += 1       
        return output 