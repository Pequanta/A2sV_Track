# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        prev = None
        cur = head
        while cur:
            lst.append(cur.val)
            hold_next = cur.next
            cur.next = prev
            prev = cur
            cur = hold_next
        i = 0
        while prev:
            if prev.val != lst[i]:
                return False
            prev = prev.next
            i += 1
        return True