class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        alpha = defaultdict(list)
        for w in words:
            alpha[w[0]].append(w)
            
        counter = 0
        for c in s:
            old_bucket = alpha[c]
            alpha[c] = []
            for w in old_bucket:
                next_word = w[1:]
                if next_word:
                    alpha[next_word[0]].append(next_word)
                else:
                    counter+=1
                    
            
        return counter