# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = [root, "$"]
        out = []
        temp_list = []

        while len(q) != 0:
            n = q.pop(0)
            if n == "$":
                if temp_list != []:
                    out.append(temp_list)
                    temp_list = []
                    q.append("$")
            else:
                temp_list.append(n.val)
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)

        return out