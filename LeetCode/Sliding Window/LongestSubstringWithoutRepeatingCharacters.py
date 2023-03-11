class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        repeating = []
        output = 0
        while (right < len(s)):
            if s[right] not in repeating:
                repeating.append(s[right])
                right += 1
                output = max(output , len(repeating))
            elif s[right] in repeating:
                repeating.pop(left)
        return output