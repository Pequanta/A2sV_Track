# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def helper(root, count, cont_rows):
            if not root:
                count -= 1
                return 
            count += 1
            if count in cont_rows:
                cont_rows[count].append(root.val)
            else:
                cont_rows[count] = [root.val]
            helper(root.left, count , cont_rows)
            helper(root.right, count, cont_rows)
            return cont_rows
        cont_rows = helper(root,0, {})
        rows = sorted(cont_rows)
        result = []
        for i in range(len(rows)):
            if i % 2 != 0:
                result.append(cont_rows[rows[i]][::-1])
            else:
                result.append(cont_rows[rows[i]])
        return result