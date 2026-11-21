# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head.next == None:
            return None
        c = 0
        temp = head
        while temp != None:
            temp =temp.next
            c += 1
        temp = head
        if c-n-1 == -1:
            return head.next
        for i in range(c-n-1):
            temp = temp.next
        temp.next = temp.next.next
        return head

        