from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def helperFunction(nums, index, size):
            if index >= size:
                return 0
            if index in dp:
                return dp[index]
            dp[index] = max(
                helperFunction(nums, index + 1, size),
                nums[index] + helperFunction(nums, index + 2, size),
            )
            return dp[index]

        return helperFunction(nums, 0, len(nums))
