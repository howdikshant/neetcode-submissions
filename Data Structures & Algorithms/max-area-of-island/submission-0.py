class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()


        def dfs(r, c, n):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == 0 or 
                (r, c) in visited
            ):
              return 0

            visited.add((r, c))
            
            return (
                1 + 
                dfs(r + 1, c, n + 1) + 
                dfs(r - 1, c, n + 1) + 
                dfs(r, c + 1, n + 1) + 
                dfs(r, c - 1, n + 1)

            )
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    
                    n = dfs(r, c, 0)
                    m = max(m, n)


        return m