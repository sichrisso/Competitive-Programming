# Method I

def sortSentence(self, s: str) -> str:
    sentence = " "
    word = s.split(" ")
    for i in range (len(word)):
        for j in range (0, len(word)-i -1):
            if word[j][-1] > word[j+1][-1]:
                word[j], word[j+1] = word[j+1], word[j]
    for i in range(len(word)):
            sentence += word[i][:-1]  + ' '
    return (sentence[1:-1])

# Method II

def sortSentence(self, s: str) -> str:  
        word = s.split(" ")
        for i in range(len(word)):
            word[i] = word[i][::-1]
        word.sort()
        for i in range(len(word)):
            word[i] = word[i][::-1][:-1]
        return " ".join(word)