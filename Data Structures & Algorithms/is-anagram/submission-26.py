class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counterT = {}
        counterS = {}

        for c in s:
            counterT[c] = 1 + counterT.get(c , 0)
        
        for c in t:
            counterS[c] = 1 + counterS.get(c , 0)
        
        return counterS == counterT
        