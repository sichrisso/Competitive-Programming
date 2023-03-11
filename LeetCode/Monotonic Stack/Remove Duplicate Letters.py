class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        mon_sta = []
        duplicate = defaultdict(int)
        for i in range(len(s)):
            if s[i] not in duplicate:
                while mon_sta and s[i] < mon_sta[-1]:
                    if count[mon_sta[-1]] > 0:
                        del duplicate[mon_sta[-1]]
                        mon_sta.pop()
                    else:
                        break
                mon_sta.append(s[i])
                duplicate[s[i]] += 1
                count[s[i]] -= 1
            else:
                count[s[i]] -= 1
        return "".join(mon_sta)


        

       