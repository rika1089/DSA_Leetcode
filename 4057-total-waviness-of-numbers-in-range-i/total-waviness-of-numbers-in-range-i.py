class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        cnt = 0

        for i in range(num1,num2+1) :
            if len(str(i)) < 3 :
                continue 
            i = str(i)
            for j in range(1,len(str(i))-1) :
                a = i[j-1]
                b = i[j]
                c = i[j+1]
                if (a<b and b>c) or (a>b and b<c) :
                    cnt += 1

        return cnt
        