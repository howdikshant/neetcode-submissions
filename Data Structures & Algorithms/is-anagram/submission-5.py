class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ls = len(s)
        lt = len(t)

        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in s:
            freq1[ord(ch) - ord('a')] += 1
        for ch in t:
            freq2[ord(ch) - ord('a')] += 1
        
        if freq1 == freq2:
            return True
        else:
            return False
        
