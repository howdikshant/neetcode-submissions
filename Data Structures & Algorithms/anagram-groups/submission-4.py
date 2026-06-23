class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmp = {}

        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1

            sb = ""
            for i in freq:
                sb += str(i)
                sb += "#"
            if sb in hmp:
                hmp[sb].append(s)
            else:
                hmp[sb] = [s]

        return list(hmp.values())
