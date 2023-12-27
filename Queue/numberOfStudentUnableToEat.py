# class Solution:
#     def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
#         st = deque(students)
#         sd = deque(sandwiches)

#         while sd:
#             i = st[0]

#             if i == sd[0]:
#                 st.popleft()
#                 sd.popleft()
#             else:
#                 if sd[0] not in st:
#                     break

#                 st.popleft()
#                 st.append(i)

#         return len(st)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front is None:
            self.rear = self.front = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next

    def dequeue(self):
        if self.front is None:
            return 0
        else:
            temp = self.front.data
            self.front = self.front.next
            return temp

    def length(self):
        cur = self.front
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length

    def getFront(self):
        return None if self.front is None else self.front.data

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentQueue = Queue()
        sandwicheQueue = Queue()
        for i in range(len(students)):
            studentQueue.enqueue(students[i])
            sandwicheQueue.enqueue(sandwiches[i])

        sandwichesLength = len(sandwiches)
        sandwicheDistributionAttempt = sandwichesLength
        while sandwicheQueue.front is not None and studentQueue.front is not None and sandwicheDistributionAttempt != 0:
            if sandwicheQueue.getFront() == studentQueue.getFront():
                sandwicheQueue.dequeue()
                studentQueue.dequeue()
                sandwichesLength -= 1
                sandwicheDistributionAttempt = sandwichesLength
            else:
                std = studentQueue.dequeue()
                studentQueue.enqueue(std)
                sandwicheDistributionAttempt -= 1
        return sandwichesLength
