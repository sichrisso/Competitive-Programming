def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
    n = len(security)
    pre = [0]*n
    post = [0]*n
    for i in range(1, n):
        if security[i-1] >= security[i]:
            pre[i] = pre[i-1] + 1
        else:
            pre[i] = 0
    for i in range(n-2, -1, -1):
        if security[i+1] >= security[i]:
            post[i] = post[i+1] + 1
        else:
            post[i] = 0
    res = []
    for i in range(n):
        if pre[i] >= time and post[i] >= time:
            res.append(i)
    return res