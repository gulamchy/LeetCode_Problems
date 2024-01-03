from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        if root:
            queue.append(root)

        while len(queue) > 0:
            childLevel = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    childLevel.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if childLevel:
                res.append(childLevel)
        return res