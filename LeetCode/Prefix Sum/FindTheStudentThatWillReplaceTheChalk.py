def chalkReplacer(self, chalk: List[int], k: int) -> int:
    prefix = [0]
    for i in range(len(chalk)):
        prefix.append(prefix[-1] + chalk[i])
    
    i, j = 0, len(prefix)-1
    k = k % prefix[j]
    while i+1 < len(prefix):
        if prefix[i+1] - prefix[i] <= k:
            k -= prefix[i+1] - prefix[i]
            i += 1
        else:
            break
    return i