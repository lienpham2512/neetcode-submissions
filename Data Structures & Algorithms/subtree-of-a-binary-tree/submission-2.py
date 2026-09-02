# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, q, p):
        if not q and not p:
            return True
        if not q or not p or q.val != p.val:
            return False
        return self.isSameTree(q.right, p.right) and self.isSameTree(q.left, p.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        res = False
        if root.val == subRoot.val:
            res = self.isSameTree(root, subRoot)
        
        return res or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)