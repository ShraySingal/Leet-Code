from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        pr = 0
        for i in range(1, len(prices)):
            s = prices[i]
            if s > b:
                pr = max(pr, s - b)
            if b > s:
                b = s
        return pr
