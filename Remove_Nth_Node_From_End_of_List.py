# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (not (head)):
            return None
        fast = head
        slow = head
        for i in range(n):
            if fast:
                fast = fast.next
            else:
                return head
        if fast == None:
            newHead = head.next
            return newHead
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        delNode = slow.next
        slow.next = delNode.next
        return head
