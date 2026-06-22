class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tl = len(t)
        sl = len(s)

        if sl != tl:
            return False

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