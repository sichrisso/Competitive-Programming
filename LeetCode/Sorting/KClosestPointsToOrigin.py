def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        i = 0
        while i < len(points):
            d = ((points[i][0])**2 + (points[i][1])**2)
            points[i].insert(0,  d)
            i += 1
        points = heapq.nsmallest(k,points)
        for i in range (len(points)):
            points[i].pop(0)
        return points