def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    prefix = [0]
    left, output = 0, 0
    right = left + k
    for i in range(len(arr)):
        prefix.append(prefix[-1] + arr[i])
    while right < len(prefix):
        if (prefix[right] - prefix[left]) // k >= threshold:
            output += 1
        left += 1
        right += 1
    return output