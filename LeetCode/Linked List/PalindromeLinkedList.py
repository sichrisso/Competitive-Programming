def isPalindrome(self, head: Optional[ListNode]) -> bool:
    current = head
    output = []
    while current:
        output.append(current.val)
        current = current.next
    left= 0
    right = len(output) - 1
    while left <= right:
        if output[left] == output[right]:
            left += 1
            right -= 1
        else:
            return False
    return True