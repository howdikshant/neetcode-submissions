class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = s[::-1]

        s1 = ""
        for ch in s:
            if ch.isalnum():
                s1 += ch
        s2 = ""
        for ch in rev:
            if ch.isalnum():
                s2 += ch

        if s1.lower() == s2.lower():
            return True

        return False


        
        