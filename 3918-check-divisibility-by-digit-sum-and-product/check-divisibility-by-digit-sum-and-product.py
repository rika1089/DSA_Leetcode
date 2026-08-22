class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # SUM = 0
        # PROD = 1
        # for digit in list(str(n)) :
        #     SUM += int(digit)
        #     PROD *= int(digit)
        
        # return n % ( SUM + PROD ) == 0 

        return  n % (sum(ln:= [(n//p)%10 for i in range(7) if (p:=10**i) <=n]) + prod(ln)) == 0