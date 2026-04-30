from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class NumArray:
    def __init__(self, nums: List[int]):
        self.num = nums
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        while left <= right:
            sum += self.num[left]
            left += 1
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
