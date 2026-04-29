class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        firstIndex = scIndex = None
        for i in range(len(s1)):
            if(s1[i] == s2[i]):
                continue
            else:
                count += 1
                scIndex = firstIndex
                firstIndex = i
            if count > 2:
                return False
        if firstIndex == None and scIndex == None:
            return True
        if scIndex == None and firstIndex != None:
            return False
        if s1[scIndex] == s2[firstIndex] and s2[scIndex] == s1[firstIndex]:
            return True
        return False
