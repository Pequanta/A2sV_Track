# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lst = []
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs_traversal(left, right):
            if left and not right:
                return False
            if right and not left:
                return False
            if not right and not left:
                return True
            if left.val != right.val:
                return False
            return dfs_traversal(left.left,  right.right) and dfs_traversal(left.right, right.left)
        return dfs_traversal(root.left, root.right)

            