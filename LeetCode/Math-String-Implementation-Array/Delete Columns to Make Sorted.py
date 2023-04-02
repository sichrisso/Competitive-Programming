class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        col = len(strs[0])
        count = 0
        for i in range(col):
            output = []
            for j in range(row):
                if len(output) == 0:
                    output.append(strs[j][i])
                else:
                    if ord(strs[j][i]) < ord(output[-1]):
                        count += 1
                        break
                    else:
                        output.append( strs[j][i])
        return count