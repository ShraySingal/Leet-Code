from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return not (len(s) == len(nums))
