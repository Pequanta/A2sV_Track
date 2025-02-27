# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cont_lst = []
        cur = head
        while cur:
            cont_lst.append(cur)
            cur = cur.next
        i = len(cont_lst) - 1
        cur = head
        max_sum = float("-inf")
        while cur and i >= len(cont_lst) // 2:
            max_sum = max(max_sum, cur.val + cont_lst[i].val)
            i -= 1
            cur = cur.next
        return max_sum
