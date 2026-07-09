# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, node):
        max_depth = 1
        l_d = 0
        r_d = 0
        if node.left is not None:
            l_d = self.depth(node.left) + 1
        if node.right is not None:
            r_d = self.depth(node.right) + 1
        if node.left is None and node.right is None:
            return 1
        
        return max(l_d, r_d)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.depth(root)