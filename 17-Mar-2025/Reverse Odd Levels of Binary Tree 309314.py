# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(left, right, count):
            if not right or not left:
                count -= 1
                return
            if count % 2 != 0:
                temp = right.val
                right.val = left.val
                left.val = temp
            count += 1
            helper(left.left, right.right, count)
            helper(left.right, right.left, count)
        helper(root.left, root.right, 1)
        return root
            
