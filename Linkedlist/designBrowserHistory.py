class Node:
    def __init__(self,url):
        self.prev = None
        self.url = url
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.cur = self.head

    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.prev = self.cur
        self.cur.next = newNode
        self.cur = newNode

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)