class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        output = []
        for i in range(26):
            chara = chr(i +97)
            count = 101
            for word in words:
                wordC=0
                for c in range(len(word)):
                    if word[c] == chara:
                        wordC+=1
                count = min(count,wordC)
            for k in range(count):
                output.append(chara)
        return output