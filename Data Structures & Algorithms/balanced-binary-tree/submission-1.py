# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_bottomUp(root):
            if root is None:
                return [True, 0]
            rightHeight = dfs_bottomUp(root.right)
            leftHeight = dfs_bottomUp(root.left)
            balance = rightHeight[0] and leftHeight[0] and abs(rightHeight[1]-leftHeight[1])<=1
            return [balance, max(rightHeight[1], leftHeight[1])+1]
        return dfs_bottomUp(root)[0]