# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        cr = 0
        H = T = None
        while l1 or l2 or cr :
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            if l1 :
                l1 = l1.next
            if l2 : 
                l2 = l2.next
            sum = temp1 + temp2 + cr
            tp = ListNode(sum % 10)
            cr = sum // 10
            if H == None :
                H = T = tp
            else :
                T.next = tp
                T = tp
        return H 
