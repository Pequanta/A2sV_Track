# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        flag = True if self.head else False
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        prev = None
        cur = self.head
        while cur:
            prev = cur
            cur = cur.next
        if not prev:
            self.head = Node(val)
        else:
            prev.next = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        prev = None
        cur = self.head
        i = 0
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            while cur:
                if i == index:
                    if not prev:
                        new_node.next = self.head
                        self.head = new_node
                    else:
                        new_node.next = cur
                        prev.next = new_node
                    return
                i += 1
                prev = cur
                cur = cur.next
            if index == i:
                prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        i = 0
        prev = None
        while cur:
            if i == index:
                if not prev and self.head:
                    self.head =self.head.next
                else:
                    prev.next = cur.next
                    cur =cur.next
                break
            i += 1
            prev = cur
            cur = cur.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)