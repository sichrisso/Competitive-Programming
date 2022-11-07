# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current  = head
        length = i = 0
        output = []
        while current:
            current = current.next
            length += 1
        current = head
        if length == 1:
            return current 
        else:
            while i != (length // 2):
                i += 1
                current = current.next
            while current:
                return current