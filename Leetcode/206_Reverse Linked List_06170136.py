# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        N_head = None
        while head!=None:
            tmp = head.next
            head.next = N_head
            N_head = head
            head = tmp
            
        return N_head
        
