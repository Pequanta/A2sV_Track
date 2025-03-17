# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        def helper(root, val):
            if root and not (root.right or root.left):
                new_node = TreeNode(val)
                if root.val < val:
                    root.right = new_node
                else:
                    root.left = new_node
                return 
            if root.val < val:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                return helper(root.right, val)
            elif root.val > val:
                if not root.left:
                    root.left = TreeNode(val)
                    return
                return helper(root.left, val)
        helper(root,val)
        return root
