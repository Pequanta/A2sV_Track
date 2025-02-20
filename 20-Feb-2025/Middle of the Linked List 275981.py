# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        size = 0
        while cur:
            size += 1
            cur =cur.next
        i = 0

        cur = head
        while cur:
            if i == (size // 2):
                return cur
            i += 1
            cur = cur.next