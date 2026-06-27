class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        res = []
        def dfs(o, c):
            if o == 0 and c == 0:
                res.append("".join(s))
                return

            if o < c:
                if o > 0:
                    s.append("(")
                    dfs(o-1, c)
                    s.pop()
                
                s.append(")")
                dfs(o, c-1)
                s.pop()

            elif o == c:
                s.append("(")
                dfs(o-1, c)
                s.pop()
        dfs(n, n)
        return res

            



