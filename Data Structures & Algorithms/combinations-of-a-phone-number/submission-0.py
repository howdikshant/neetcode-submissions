class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmp = {}
        hmp[2] = "abc"
        hmp[3] = "def"
        hmp[4] = "ghi"
        hmp[5] = "jkl"
        hmp[6] = "mno"
        hmp[7] = "pqrs"
        hmp[8] = "tuv"
        hmp[9] = "wxyz"
        res = []

        if not digits:
            return []
        def dfs(curr, i):
            if i == len(digits):
                res.append(curr)
                return
            for ch in hmp[int(digits[i])]:
                dfs(curr+ch, i+1)

        dfs("", 0)
        return res
                

