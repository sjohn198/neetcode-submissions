# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def printList(self, node):
    #     if node is None:
    #         return
    #     print(node.val)
    #     self.printList(node.next)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        ptr = None
        while list1 or list2:
            # print("L1")
            # self.printList(list1)
            # print("L2")
            # self.printList(list2)
            # print("L3")
            # self.printList(merged)
            if not merged:
                if list2 is None:
                    merged = list1
                    return merged
                if list1 is None:
                    merged = list2
                    return merged
                if list1.val < list2.val:
                    temp = list1.next
                    list1.next = None
                    merged = list1
                    ptr = merged
                    list1 = temp
                else:
                    temp = list2.next
                    list2.next = None
                    merged = list2
                    ptr = merged
                    list2 = temp
            else:
                if list2 is None:
                    ptr.next = list1
                    return merged
                if list1 is None:
                    ptr.next = list2
                    return merged
                if list1.val < list2.val:
                    temp = list1.next
                    list1.next = None
                    ptr.next = list1
                    ptr = ptr.next
                    list1 = temp
                else:
                    temp = list2.next
                    list2.next = None
                    ptr.next = list2
                    ptr = ptr.next
                    list2 = temp

        return merged