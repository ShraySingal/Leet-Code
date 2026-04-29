
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for data in nums:
            if data in d :
                d[data ] += 1
            else:
                d[data] = 1
        size = len(nums)
        for key in d:
            count = d[key]
            if count > (size // 2) or count >= (size // 2) and size % 2 == 0:
                return key
