def partitionLabels(self, s: str) -> List[int]:
    dict = {}
    part = count = 0
    output = []
    for i in range(len(s)):
        dict[s[i]] = i
    for i in range(len(s)):
        part = max(part, dict[s[i]])  
        count += 1       
        if i == part:
            output.append(count)
            count = 0 
    return output