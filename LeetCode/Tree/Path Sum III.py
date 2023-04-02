# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.output = 0
        self.dict = {0:1}
        def targetsum(node, sumSofar):
            if not node:
                return 
            sumSofar += node.val
            if sumSofar - targetSum in self.dict:
                self.output += self.dict[ sumSofar - targetSum]
            if sumSofar in self.dict:
                self.dict[sumSofar] += 1
            else:
                self.dict[sumSofar] = 1
            
            targetsum(node.left, sumSofar)
            targetsum(node.right, sumSofar)
            self.dict[sumSofar] -= 1
            
        targetsum(root, 0)
        return self.output