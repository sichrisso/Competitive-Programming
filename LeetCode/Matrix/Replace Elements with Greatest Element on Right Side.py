class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        s, x, y = 0, 0, 0
        while x != len(arr)-1:
            for i in range(x+1, len(arr)):
                if s < arr[i]:
                    s = arr[i]
                    x = i
            for i in range(y, x):
                arr[i] = s
            s = 0
            y = x
        arr.pop()
        arr.append(-1)
        return arr