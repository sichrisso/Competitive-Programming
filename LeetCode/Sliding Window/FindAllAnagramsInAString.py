def findAnagrams(self, s: str, p: str) -> List[int]:
    output = []
    left = right = 0
    P = Counter(p)
    while right < len(s):
        if right == 0:
            anagram = Counter(s[right : right + len(p)])
            right += len(p)
        else:
            anagram[s[left]] -= 1
            anagram[s[right]] += 1
            left += 1
            right += 1
        if anagram == P:
            output.append(left)
    return output