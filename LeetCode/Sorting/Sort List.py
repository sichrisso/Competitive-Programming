# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return

        node, l = head, [[head.val, head]]
        while node.next:
            node = node.next
            l.append([node.val, node])
            
        l.sort(key=lambda x:x[0])
		
        node = head = l[0][1]
        for k,v in l[1:]:
            node.next = v
            node = node.next
        node.next = None
        return head