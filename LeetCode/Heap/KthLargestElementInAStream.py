class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = nums[:min(k, len(nums))]
        heapify(self.pq)
        for i in range(k, len(nums)):
            heappushpop(self.pq, nums[i])


    def add(self, val: int) -> int:
        heappush(self.pq, val)
        if len(self.pq) > self.k : heappop(self.pq)
        return self.pq[0]
        
        
