# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_height(self, node) -> int:
        if node is None or (node.left is None and node.right is None):
            return 1
        if node.left is None:
            return 1 + self.get_height(node.right)
        elif node.right is None:
            return 1 + self.get_height(node.left)
        else:
            return max(1 + self.get_height(node.left), 1 + self.get_height(node.right))

    def traversal(self, node) -> int:
        leftHeight = 0
        rightHeight = 0
        l_diam = 0
        r_diam = 0
        if node.left is not None:
            leftHeight = self.get_height(node.left)
            l_diam = self.traversal(node.left)
        if node.right is not None:
            rightHeight = self.get_height(node.right)
            r_diam = self.traversal(node.right)
        diameter = leftHeight + rightHeight
        return max(diameter, r_diam, l_diam)

        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.traversal(root)
        
        
              