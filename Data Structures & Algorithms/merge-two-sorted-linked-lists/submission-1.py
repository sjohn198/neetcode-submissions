# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        head = None
        tail = None
        while list1 is not None or list2 is not None:
            if list1 is None:
                if head is None:
                    return list2
                else:
                    tail.next = list2
                    return head
            if list2 is None:
                if head is None:
                    return list1
                else:
                    tail.next = list1
                    return head
            if list1.val <= list2.val:
                if head is None:
                    head = list1
                    tail = list1
                else:
                    tail.next = list1
                    tail = tail.next
                list1 = list1.next
            else:
                if head is None:
                    head = list2
                    tail = list2
                else:
                    tail.next = list2
                    tail = tail.next
                list2 = list2.next