def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    n = len(arr)
    prefix = [0 for _ in range(n + 1)]
    for i in range(n):
        prefix[i+1] = prefix[i] ^ arr[i]
    res = []
    for l, r in queries:
        res.append(prefix[r + 1] ^ prefix[l])
    return res
    