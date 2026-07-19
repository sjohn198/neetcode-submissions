# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        nodes = {}
        i = 0
        cur_node = head
        while cur_node:
            nodes[i] = cur_node
            cur_node = cur_node.next
            i += 1
        length = i
        final_list = head
        ptr = final_list
        left = 1
        right = length - 1
        for n in range(1, length):
            if n % 2 == 1:
                ind = right
                right -= 1
            else:
                ind = left
                left += 1
            nodes[ind].next = None
            ptr.next = nodes[ind]
            ptr = ptr.next
        head = final_list