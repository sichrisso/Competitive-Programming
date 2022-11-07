def maxScore(self, cardPoints: List[int], k: int) -> int:
    left = sum = output = 0
    right = n = len(cardPoints) - 1
    prefix = []
    for i in range(len(cardPoints)):
        if len(prefix) == 0:
            prefix.append(cardPoints[i])
        else:
            prefix.append(prefix[-1] + cardPoints[i])
    for i in range(len(prefix)):
        if i < n - k:
            pass
        elif i == n - k:
            output = max(output, prefix[right] - prefix[i])
        else:
            sum += cardPoints[left]
            output = max(output, prefix[right] - prefix[i] + sum)
            left += 1
    return output 