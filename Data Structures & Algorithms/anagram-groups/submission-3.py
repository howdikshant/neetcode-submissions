class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmp = {}
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1

            key = tuple(freq)

            if key not in hmp:
                hmp[key] = []
            hmp[key].append(s)

        arr = list(hmp.values())
        return arr

