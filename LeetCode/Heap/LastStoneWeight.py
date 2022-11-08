def lastStoneWeight(self, stones: List[int]) -> int:
    sl = SortedList(stones)
    while len(sl) >= 2:
        y = sl.pop()
        x = sl.pop()
        if y > x: sl.add(y - x)  # Note that sl is a SortedList
    return sl.pop() if len(sl) else 0