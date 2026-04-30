from typing import List, Optional, Dict, Tuple, Set
from collections import deque, defaultdict
import heapq

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while(start <= end):
            while start <= end and  (not s[start].isalnum()):
                start = start + 1
            while start <= end and (not s[end].isalnum()):
                end = end - 1
            if start <= end and  s[start].lower() != s[end].lower():
                return False
            start = start + 1
            end = end - 1
        else :
                return True
