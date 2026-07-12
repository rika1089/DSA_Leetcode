class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[-1][-1] >= 0 :
            return 0

        i = m - 1
        j = 0
        cnt = 0

        while i>=0 and j<n :
            if grid[i][j] < 0 :
                cnt += n - j
                i -= 1
            else :
                j += 1

        return cnt
        




                