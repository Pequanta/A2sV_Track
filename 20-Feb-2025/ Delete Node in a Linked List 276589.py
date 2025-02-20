# Problem:  Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        prev = None

        while cur:
            if not cur.next:
                prev.next = None
                break
            if prev:
                prev.val = cur.val
            cur.val = cur.next.val
            prev = cur
            cur = cur.next
