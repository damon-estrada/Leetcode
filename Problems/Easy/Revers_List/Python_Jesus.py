# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is not None:
            # gonna need two additional pointers for this one to keep track of the previous head and one to keep track of the next head
            pt_back = head

            if head.next is not None:
                head = head.next

            pt_back.next = None
            while head.next is not None:
                pt_front = head.next
                head.next = pt_back
                pt_back = head
                head = pt_front

            # Just swap and return the list
            if head != pt_back:
                head.next = pt_back

        return head