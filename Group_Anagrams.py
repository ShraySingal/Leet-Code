class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            data = ''.join(sorted(i))   
            if data in d:
                d[data].append(i)      
            else:
                d[data] = [i]

        return list(d.values()).    
