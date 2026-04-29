# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs_bottomUp(root):
            if root is None:
                return 0
            rightDepth = dfs_bottomUp(root.right)
            leftDepth = dfs_bottomUp(root.left)
            self.diameter = max(self.diameter, rightDepth+leftDepth)
            return max(rightDepth, leftDepth)+1
        dfs_bottomUp(root)
        return self.diameter