# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        prev = None
        cur = l1
        while cur and l2:
            temp_sum = cur.val + l2.val + carry
            carry = temp_sum // 10
            cur.val = temp_sum % 10
            prev = cur
            cur = cur.next
            l2 = l2.next
        if l2:
            prev.next = l2
        if carry != 0:
            cur = prev.next
            while cur:
                temp_sum = cur.val + carry
                cur.val = temp_sum % 10
                carry = temp_sum // 10
                prev = cur
                cur = cur.next
            if carry != 0 and prev:
                new_node = ListNode(carry)
                prev.next = new_node
                
        return l1

