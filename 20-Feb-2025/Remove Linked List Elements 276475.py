# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            if cur.val == val:
                if not prev:
                    head = head.next
                else:
                    prev.next = cur.next
                cur = cur.next
                continue
            prev = cur
            cur = cur.next
        return head