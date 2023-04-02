# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        output = []
        curr = head
        while curr:
            output.append(curr.val)
            curr = curr.next
   
        l , r = 0, len(output)-1
        twinSum = 0
        while l < r:
            twinSum = max(twinSum, output[l] + output[r])
            l += 1
            r -= 1
        return twinSum