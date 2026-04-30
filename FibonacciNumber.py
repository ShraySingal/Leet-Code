from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
