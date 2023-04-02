# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(curr, lower, upper):
            if not curr:
                return True
            if lower >= curr.val or upper <= curr.val:
                return False
            else:
                Left = valid(curr.left, lower, curr.val)
                Right = valid(curr.right, curr.val, upper)
                return Left and Right
        return valid(root, float('-inf'), float('inf'))
            

     