class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.rear is None:
            self.rear = self.front = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        else:
            temp = self.front.data
            self.front = self.front.next
            return temp
        
    def display(self):
        if self.front is None:
            return "Queue is empty"
        else:
            cur = self.front
            while cur:
                cur = cur.next
            return cur
        
    def isEmpty(self):
        return self.front is None
    
    def sizeOfQueue(self):
        count = 0
        cur = self.front
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def frontAndRearData(self):
        return self.front.data, self.rear.data
