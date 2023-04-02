class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        left, right = 0, 0
        n, m = len(word1), len(word2)
        output = []
        while left < n and right < m:
            word_1 = word1[left:]
            word_2 = word2[right:]
            if word_1 > word_2:
                output.append(word1[left])
                left += 1
            else:
                output.append(word2[right])
                right += 1  
        output.extend(word1[left:])
        output.extend(word2[right:])
        return "".join(output)
            