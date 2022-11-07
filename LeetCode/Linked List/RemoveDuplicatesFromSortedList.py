def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    output = []
    while current:
        if current.val in output:
            pass
        else:
            output.append(current.val)
        current = current.next
    dummy = current = ListNode()
    for i in output:
        current.next = ListNode(i)
        current = current.next 
    return dummy.next