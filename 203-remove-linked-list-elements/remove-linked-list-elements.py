# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        temp = head

        while temp:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next

        return dummy.next


                
        