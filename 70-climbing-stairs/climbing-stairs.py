class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(i) :
            if i in memo :
                return memo[i]
            if i == n :
                return 1

            if i > n :
                return 0
            
            oneStep = climb(i+1)
            twoStep = climb(i+2)

            memo[i] = oneStep + twoStep

            return memo[i]
        
        return climb(0)
                