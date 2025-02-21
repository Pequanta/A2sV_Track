# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even = head
        odd = head.next
        

        even_cur = even
        odd_cur = odd
        prev = None
        while even_cur and odd_cur and even_cur.next and odd_cur.next:
            prev = even_cur
            even_cur.next = odd_cur.next
            even_cur = even_cur.next
            odd_cur.next = even_cur.next
            odd_cur = odd_cur.next

        if even_cur:
            prev = even_cur
            even_cur = even_cur.next
        prev.next = odd
        return even
