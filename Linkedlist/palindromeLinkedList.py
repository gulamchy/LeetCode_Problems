# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseLinkedList(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        middle = end = head
        while end and end.next:
            middle = middle.next
            end = end.next.next
        
        reverseHalfList = reverseLinkedList(middle)

        while reverseHalfList:
            if head.val != reverseHalfList.val:
                return False
            head = head.next
            reverseHalfList = reverseHalfList.next
        
        return True