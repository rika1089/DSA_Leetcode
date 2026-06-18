from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0":
                return
            grid[i][j] = "0"  # mark visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands
