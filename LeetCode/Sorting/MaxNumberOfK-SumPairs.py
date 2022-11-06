def maxOperations(self, nums: List[int], k: int) -> int:
        output = 0
        pairs = Counter(nums)
        seen = set()
        for i in pairs:
            if i not in seen and k-i in pairs:
                if i == k-i:
                    output += pairs[i]//2
                else:
                    output += min(pairs[i], pairs[k-i])
            seen.add(i)
            seen.add(k-i)
        return output