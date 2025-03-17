# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        cont_max = {}

        def helper(root, count, cont_max):
            if not root:
                count -= 1
                return 
            if count in cont_max:
                cont_max[count] = max(cont_max[count], root.val)
            else:
                cont_max[count] = root.val
            count += 1
            helper(root.left, count , cont_max)
            helper(root.right, count, cont_max)
        helper(root, 1, cont_max)
        vals = sorted(cont_max.keys())
        result = []
        for val in vals:
            result.append(cont_max[val])
        return result
