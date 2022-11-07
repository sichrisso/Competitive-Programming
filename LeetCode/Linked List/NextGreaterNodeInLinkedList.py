def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    currInd  = 0
    result = []
    stack = []
    while head:
        result.append(0)
        while stack and stack[-1][1] < head.val:
            overwriteInd, nodeVal = stack.pop()
            result[overwriteInd] = head.val
        stack.append((currInd, head.val))
        currInd += 1
        head = head.next
    return result