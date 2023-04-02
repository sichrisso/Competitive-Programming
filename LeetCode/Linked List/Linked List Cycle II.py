# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = -1
        index = {}
        while curr:
            count += 1
            if curr in index:
               return curr
            else:
                index[curr] = count
            curr = curr.next
        return None