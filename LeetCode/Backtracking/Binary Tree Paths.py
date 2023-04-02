# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        def backTracking(root, hold):
            if root.left == None and root.right == None:
                output.append(hold)

            if root.left:
                backTracking(root.left, hold + "->" + str(root.left.val)) 

            if root.right:
                backTracking(root.right, hold + "->" + str(root.right.val)) 
        
        backTracking(root, str(root.val))
        return output

       