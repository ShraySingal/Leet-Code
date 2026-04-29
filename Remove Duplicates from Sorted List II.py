# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = tm = head.next
        if head == None:
            return None
        while p :
            if p and tm.next and p.val == tm.next.val :
                tm = tm.next
            elif p == tm :
                p = p.next
                tm = tm.next
            else :
                tm = p
                p.next = p.next.next
        return head
            
