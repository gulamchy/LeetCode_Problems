# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
            
        # Recursion
        # res = []
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return res