# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class MyStack:

#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def push(self, x: int) -> None:
#         if self.rear is None:
#             self.rear = self.front = Node(x)
#         else:
#             self.rear.next = Node(x)
#             self.rear = self.rear.next

#     def pop(self) -> int:
#         if self.rear is None:
#             return 
#         elif self.front == self.rear:
#             temp = self.rear.data
#             self.front = self.rear = None
#             return temp
#         else:
#             temp = self.rear.data
#             cur = self.front
#             while cur.next is not self.rear:
#                 cur = cur.next
#             self.rear = cur
#             return temp


#     def top(self) -> int:
#         return self.rear.data

#     def empty(self) -> bool:
#         return self.front is None

from collections import deque

class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        return self.stack.pop()


    def top(self) -> int:
        if self.empty():
            return None
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()