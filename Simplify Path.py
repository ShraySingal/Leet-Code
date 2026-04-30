from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for val in path:
            if val == "" or val == ".":
                continue
            elif val == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(val)
        return "/" + ("/".join(stack))
