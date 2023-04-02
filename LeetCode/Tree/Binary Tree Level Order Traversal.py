# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = defaultdict(list)
        output = []
        def dfs(root, level):
            if not root:
                return
            dict[level].append(root.val)
            Left = dfs(root.left, level + 1)
            Right = dfs(root.right, level + 1) 

        dfs(root, level = 0)
        for i in sorted(dict.keys()):
            output.append(dict[i])
        return output