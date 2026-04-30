from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp = n
        rev = 0
        while n:
            rev = (rev * 10) + (n % 10)
            n //= 10
        return abs(temp - rev)
