class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0)+1
        freq1 = {}
        for j in t:
            freq1[j] = freq1.get(j,0)+1
        
        return freq == freq1