from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for val in s:
            if stack and stack[-1] == val:
                stack.pop()
            else:
                stack.append(val)
        return "".join(stack)
