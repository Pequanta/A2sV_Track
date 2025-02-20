# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        prev = None
        first_cur = list1
        second_cur = list2
        while first_cur and second_cur:
            if first_cur.val > second_cur.val:
                hold_second = second_cur
                second_cur = second_cur.next
                if not prev:
                    hold_second.next = first_cur
                    list1 = hold_second
                    prev = hold_second
                else:
                    prev.next = hold_second
                    hold_second.next = first_cur
                    prev = hold_second
            else:
                prev = first_cur
                first_cur = first_cur.next  
        if second_cur:
            prev.next =second_cur
        return list1