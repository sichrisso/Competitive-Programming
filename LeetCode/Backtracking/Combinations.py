class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def backTracking(start, hold):
            if len(hold) == k:
                output.append(hold.copy())
                return
                
            for i in range(start, n+1):
                hold.append(i)
                backTracking(i+1, hold)
                hold.pop()
        backTracking(1, [])
        return output

       