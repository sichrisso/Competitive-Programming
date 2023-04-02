# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = -1
        dummy1 = even = ListNode()
        dummy2 = odd = ListNode()
        while curr:
            count += 1
            if count % 2 == 0:
                even.next = ListNode(curr.val)
                even = even.next
            else:
                odd.next = ListNode(curr.val)
                odd = odd.next
            curr = curr.next
        even.next = dummy2.next
        return dummy1.next