# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        temp = []
        duplicate = None
        dummy = output = ListNode()
        while current:
            value = current.val
            if len(temp) == 0 and duplicate == None:
                temp.append(value)
            elif value not in temp and value != duplicate:
                temp.append(value)
            elif value in temp:
                duplicate = value
                temp.remove(value)
            else:
                pass
            current = current.next
        for i in temp:
            output.next = ListNode(i)
            output = output.next
        return dummy.next
            
        
            
        