class Solution:
    def checkDivisibility(self, n: int) -> bool:
        SUM = 0
        PROD = 1
        for digit in list(str(n)) :
            SUM += int(digit)
            PROD *= int(digit)
        
        return n % ( SUM + PROD ) == 0 