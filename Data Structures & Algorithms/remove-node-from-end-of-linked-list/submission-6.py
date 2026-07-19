# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        cur_node = head

        while cur_node:
            temp_ptr = cur_node
            for i in range(n+1):
                if temp_ptr is None:
                    head = head.next
                    print(head.val)
                    return head
                temp_ptr = temp_ptr.next
            if temp_ptr is None:
                if cur_node.next is not None:
                    cur_node.next = cur_node.next.next
                break
            cur_node = cur_node.next
        return head
