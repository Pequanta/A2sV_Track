# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        index = 1
        d_head = head
        d_prev = None
        while d_head:
            if index == left:
                prev = None
                cur = d_head
                first_time = True
                hold_cur = None
                while cur and index <= right:
                    if first_time:
                        hold_cur = cur
                        first_time = False
                    hold_next = cur.next
                    cur.next = prev
                    prev = cur
                    cur = hold_next
                    index += 1
                hold_cur.next = cur
                if d_prev:
                    d_prev.next = prev
                else:
                    head = prev
                break
            index += 1
            d_prev = d_head
            d_head = d_head.next
        return head