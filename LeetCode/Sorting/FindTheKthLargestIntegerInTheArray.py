def kthLargestNumber(self, nums: List[str], k: int) -> str:
        output = []
        for i in nums:
            output.append(int(i))
        output = heapq.nlargest(k, output)
        return str(output[-1])