class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        def dfs(i):
            if i == len(s):
                res.append(sub.copy())
                return

            for j in range(i, len(s)):
                curr = s[i:j+1]
                if curr == curr[::-1]:
                    sub.append(curr)
                    dfs(j+1)
                    sub.pop()
        dfs(0)

        return res




