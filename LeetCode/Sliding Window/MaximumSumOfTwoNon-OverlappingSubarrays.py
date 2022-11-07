def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
    p1 = p2 = p3 = p4 = 0
    output1 = output2 = sumMax1 = sumMax2 = 0
    prefix = [0]
    for i in range(len(nums)):
        prefix.append(prefix[-1] + nums[i])
    while p2 + firstLen + secondLen < len(prefix) and p4 + firstLen + secondLen < len(prefix) :
        sumMax1 = max(sumMax1, prefix[p1 + secondLen] - prefix[p1])
        output1 = max(output1, (sumMax1) + (prefix[p2 + firstLen + secondLen] - prefix[p1 + secondLen]))
        p1 += 1
        p2 += 1
        sumMax2 = max(sumMax2, prefix[p3 + firstLen] - prefix[p3])
        output2 = max(output2, (sumMax2) + (prefix[p4 + firstLen + secondLen] - prefix[p3 + firstLen]))
        p3 += 1
        p4 += 1
    return max(output1, output2)