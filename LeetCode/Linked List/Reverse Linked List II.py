# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.next
        rev = output[left-1:right]
        rev = rev[::-1]
       
        output[left-1:right] = rev
        dummy = point = ListNode()
        for i in output:
            point.next = ListNode(i)
            point = point.next
        return dummy.next
    