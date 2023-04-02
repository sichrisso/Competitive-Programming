# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        index = {}
        while curr:
            if curr in index:
               return True
            else:
                index[curr] = 1
            curr = curr.next
        return False