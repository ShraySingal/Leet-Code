from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        index = 0
        while index < len(nums):
            res = target - nums[index]
            if res in num_map:
                return [num_map[res], index]
            num_map[nums[index]] = index
            index += 1
        return []
