# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        cur = head
        prev = None

        found = False
        hold_nodes = []
        while cur:
            if cur.val < x:
                hold_nodes.append(cur)
                if not prev:
                    head = head.next
                else:
                    prev.next = cur.next
                cur = cur.next
                continue
            prev = cur
            cur = cur.next
        for i in range(len(hold_nodes) - 1):
            hold_nodes[i].next = hold_nodes[i + 1]
        if len(hold_nodes):
            hold_nodes[-1].next = head
            return hold_nodes[0]
        return head

        