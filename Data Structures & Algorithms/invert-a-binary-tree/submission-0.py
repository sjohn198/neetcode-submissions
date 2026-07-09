# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recHelper(self, node):
        if node is None or (node.left is None and node.right is None):
            return
        self.recHelper(node.left)
        self.recHelper(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recHelper(root)
        return root