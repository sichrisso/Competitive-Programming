# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = defaultdict(list)
        output = []
        def dfs(root, row, col):
            if not root:
                return
            dict[col].append((row, root.val))
            Left = dfs(root.left, row + 1, col - 1)
            Right = dfs(root.right, row + 1, col + 1) 

        dfs(root, row = 0, col = 0)
        for i in sorted(dict.keys()):
            sort_tuple = []
            for val in sorted(dict[i]):
                sort_tuple.append(val[1])
            output.append(sort_tuple)
        return output
         