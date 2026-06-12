class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        v = ""
        for ch in s:
            if ch != " " and ch.isalnum():
                v += ch

        

        rev = v[::-1]

        return v.upper() == rev.upper()