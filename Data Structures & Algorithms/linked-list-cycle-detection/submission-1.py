# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        nodes = set()

        cur_node = head
        while cur_node:
            if cur_node.next in nodes:
                return True
            if cur_node.next is None:
                return False
            else:
                nodes.add(cur_node)
            cur_node = cur_node.next