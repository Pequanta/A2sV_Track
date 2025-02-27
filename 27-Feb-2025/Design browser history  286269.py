# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current_page = None
    def visit(self, url: str) -> None:
        new_node = Node(url)
        if self.current_page and self.current_page.prev:
            new_node.next = self.current_page
            self.current_page.prev = new_node
            new_node.prev = self.current_page.prev
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.current_page = new_node

    def back(self, steps: int) -> str:
        i = steps
        if self.current_page:
            cur =self.current_page.next
            while cur and i > 0:
                self.current_page = cur
                cur = cur.next
                i -= 1
            return self.current_page.val
        else:
            return self.head.val
        

    def forward(self, steps: int) -> str:
        i = steps
        if self.current_page:
            cur = self.current_page.prev
            while cur and i > 0:
                self.current_page = cur
                cur = cur.prev
                i -= 1
            return self.current_page.val
        else:
            return self.head.val
       
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)