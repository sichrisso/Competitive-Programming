class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:     
        output = [0] * (len(s) + 1)
        for i in range(len(shifts)):
            if shifts[i][2] == 0:
                output[shifts[i][0]] -= 1
                output[shifts[i][1]+1] += 1
            else:
                output[shifts[i][0]] += 1
                output[shifts[i][1]+1] -= 1
      
        for i in range(1, len(output)):
            output[i] += output[i-1]
    
        ans = []
        for j in range(len(s)):
            letter = ord(s[j]) + output[j]
            letter = (letter - 97) % 26
            letter += 97
            ans.append(chr(letter))
        return "".join(ans)
         



