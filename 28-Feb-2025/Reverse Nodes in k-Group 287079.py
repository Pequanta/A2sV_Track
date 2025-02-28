# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cont_lst = []

        cur = head
        while cur:
            cont_lst.append(ListNode(cur.val))
            cur = cur.next
        left = 0
        head = cont_lst[k - 1]
        last_element = None

        for right in range(k - 1 , len(cont_lst), k):
            for temp in range(right, left, -1):
                cont_lst[temp].next = cont_lst[temp - 1]
                last_element = cont_lst[temp - 1]
            hold = left
            left = right + 1
        for i in range(0, len(cont_lst), k):
            if i + (2 * k - 1) < len(cont_lst):
                cont_lst[i].next = cont_lst[i + (2 * k- 1)]
        if len(cont_lst) % k != 0:
            end_pt = (len(cont_lst) // k) * k
            last_element.next = cont_lst[end_pt]
            i = end_pt
            while i < len(cont_lst) - 1:
                cont_lst[i].next = cont_lst[i + 1]
                i += 1
        return head
