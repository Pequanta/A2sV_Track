# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            if prev and prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
                continue
            prev = cur
            cur = cur.next
        return head 