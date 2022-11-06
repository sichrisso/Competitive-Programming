def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        output = []
        while (n != 0):
            large = max(arr)
            place = arr.index(large)
            arr[:place + 1] = reversed(arr[: place + 1])
            output.append(place + 1)
            arr.reverse()
            output.append(n+1)
            n -= 1
            arr = arr[:n+1]
        return output