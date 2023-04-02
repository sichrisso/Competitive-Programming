# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict = defaultdict(int)
        curr = root
        output = []
        def mode(curr):
            if curr == None:
                return None    
            mode(curr.left)
            dict[curr.val] += 1
            mode(curr.right)
        mode(curr) 
        maxVal = max(dict.values())
        for i in dict:
            if dict[i] == maxVal:
                output.append(i)
        return output
            