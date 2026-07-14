class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = []
        col_sum = []
        cnt = 0
        for row in mat :
            row_sum.append(sum(row))
        
        for col in zip(*mat) :
            col_sum.append(sum(col))

    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    cnt += 1

        
        return cnt
