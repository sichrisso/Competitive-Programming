class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)
        buildable = set()

        for w in words:
            pre = w[:-1]
            if not pre or pre in buildable:
                buildable.add(w)

        res = ''
        for w in buildable:
            if len(w) > len(res) or (len(w) == len(res) and w < res):
                res = w
        return res