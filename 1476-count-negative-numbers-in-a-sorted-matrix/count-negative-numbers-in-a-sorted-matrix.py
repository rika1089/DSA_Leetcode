class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0

        if grid[-1][-1] >= 0 :
            return 0

        for i in range(len(grid)-1,-1,-1) :

            for j in range(len(grid[0])-1,-1,-1) :

                if grid[i][j] < 0 :

                    cnt += 1
        
        return cnt




                