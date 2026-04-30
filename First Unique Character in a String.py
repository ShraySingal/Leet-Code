from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for val in s:
            if(val in m):
                m[val]+= 1
            else:
                m[val] = 1
        for val in m:
            if m[val] == 1:
                return s.index(val)
        return -1
