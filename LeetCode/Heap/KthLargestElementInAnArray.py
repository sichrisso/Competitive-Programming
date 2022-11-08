def findKthLargest(self, nums: List[int], k: int) -> int:
    heap_ar = []
    for ind,ele in enumerate(nums):
        if ind > k-1:
            heapq.heappushpop(heap_ar, ele)
        else:
            heapq.heappush(heap_ar,ele)

    return heap_ar[0]