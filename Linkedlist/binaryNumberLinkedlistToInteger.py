# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ""
        cur_node = head
        while cur_node is not None:
            res += str(cur_node.val)
            cur_node = cur_node.next
        return int(res,2)
    
    # Second way of results..
    # Not done by me though.. 
    # It has faster run time..
        # cur = head
        # res = 0
        # while cur:
        #     res = res * 2 + cur.val
        #     cur = cur.next
        # return res