# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            left_sub = root.left
            right_sub = root.right

            self.insertIntoBST(left_sub, right_sub)

            return left_sub

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root
        
    def insertIntoBST(self, root: Optional[TreeNode], left) -> Optional[TreeNode]:
        if not root:
            return left

        if root.val < left.val:
            root.right = self.insertIntoBST(root.right, left)
        elif root.val > left.val:
            root.left = self.insertIntoBST(root.left, left)

        return root            