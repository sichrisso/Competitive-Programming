def longestMountain(self, arr: List[int]) -> int:
    output, i, j, up, down = 0, 0, 0, 1, 1
    while j < len(arr) - 1:
        if arr[j] == arr[j+1]:
            j += 1
            i += 1
        while j < len(arr) - 1:
            if arr[j] < arr[j+1]:
                up = 0
                j += 1
            else:
                break
        while j < len(arr) - 1:
            if arr[j] > arr[j+1]:
                down = 0
                j += 1
            else:
                break
        if up == 0 and down == 0:
            output = max(output, j-i+1)
        i = j
        down = 1
        up = 1
    return output