class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        right = 0
        left = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            if s[right] not in seen:
                seen.add(s[right])
                count = max(count, len(seen))
                right += 1
        return count






            
            


        