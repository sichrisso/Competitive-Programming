# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = 0
        def check_smallest(root, k):
            if root == None:
                return None
            
            check_smallest(root.left, k)  
            self.count += 1 
            if self.count == k:
                self.ans = root.val 
            check_smallest(root.right, k)
        check_smallest(root, k)
        return self.ans
       
        
        
        
        
        