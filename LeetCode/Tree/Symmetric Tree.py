# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        node = root
        def isMirror(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val == right.val:
                left_sym = isMirror(left.left, right.right) 
                right_sym = isMirror(left.right, right.left)
                return left_sym and right_sym
            else:
                return False
        return isMirror(node.left, node.right)