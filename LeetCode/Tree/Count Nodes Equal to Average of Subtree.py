# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.output = 0
        
        def add(root):
            if not root:
                return 0, 0
            
            sum_left, size_left = add(root.left)
            sum_right, size_right = add(root.right)
            
            sum_ = sum_left + sum_right + root.val
            size = size_left + size_right + 1
            
            if sum_ // size == root.val:
                self.output += 1
                
            return sum_, size

        add(root)
        return self.output