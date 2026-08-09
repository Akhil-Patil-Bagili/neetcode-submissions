# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        count = 0

        def dfs(node):
            nonlocal count, result
            if not node or result is not None:
                return
            
            dfs(node.left)
            if result is not None:
                return
            count += 1
            if count == k:
                result = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return result