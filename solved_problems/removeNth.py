# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        pt1 = head
        pt2 = head
        k = 1
        while k!=n:
            pt2 = pt2.next
            k += 1
        pt2 = pt2.next
        if pt2:
            while pt2 and pt2.next:
                pt2 = pt2.next
                pt1 = pt1.next
            pt1.next = pt1.next.next
            return head
        else:
            head = head.next
            return head