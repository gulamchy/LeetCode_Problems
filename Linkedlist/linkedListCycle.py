# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow = fast = head
        # while fast and fast.next:
        #     if slow == fast:
        #          return True
        #     slow = slow.next
        #     fast = fast.next.next
        # return False
        hashSet = set()
        cur = head

        while cur:
            if cur in hashSet:
                return True
            hashSet.add(cur)
            cur = cur.next
        return False