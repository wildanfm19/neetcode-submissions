class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        counterS = {}
        counterT = {}

        for c in s:
            counterS[c] = counterS.get(c , 0) + 1
        
        for c in t:
            counterT[c] = counterT.get(c , 0) + 1
        
        return counterS == counterT
        