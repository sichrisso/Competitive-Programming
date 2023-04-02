class Solution:
    def hIndex(self, citations: List[int]) -> int:
        mid, l, r = 0, 0, len(citations)

        while l <= r:
            mid = (l + r)//2
            place = bisect_left(citations, mid)
            if len(citations) - place >= mid:
                l = mid + 1
            else:
                r = mid - 1
        return r