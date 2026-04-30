from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            data = ''.join(sorted(i))   
            if data in d:
                d[data].append(i)      
            else:
                d[data] = [i]

        return list(d.values())
