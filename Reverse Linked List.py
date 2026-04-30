from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        while head:
            temp = head
            head = head.next

            temp.next = p
            p = temp
        return p
