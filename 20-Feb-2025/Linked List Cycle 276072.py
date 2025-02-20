# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        pt_one = head
        pt_two = head.next.next
        while pt_two and pt_two.next:
            if pt_one == pt_two:
                return True
            pt_one = pt_one.next
            pt_two = pt_two.next.next

        return False