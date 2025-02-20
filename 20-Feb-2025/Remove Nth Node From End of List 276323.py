# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size= 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        prev = None
        cur = head
        while cur:
            if size == n:
                if not prev:
                    head = head.next
                else:
                    prev.next = cur.next
                    cur = cur.next
                break
            prev = cur
            cur = cur.next
            size -= 1
        return head