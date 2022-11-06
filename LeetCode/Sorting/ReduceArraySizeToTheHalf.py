def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        c = Counter(arr)
        for i in reversed(sorted(c.values())):
            n -= i
            count += 1
            if n <= len(arr)//2: 
                break
        return count
       