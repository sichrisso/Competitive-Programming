def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    output = 0
    while left != right:
        area = (right - left) * min(height[left], height[right])
        output = max(output, area)
        if (height[left] < height[right]):
            left += 1
        elif (height[right] < height[left]):
            right -= 1
        else:
            left += 1
    return output
    