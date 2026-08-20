class Solution:
    def tribonacci(self, n: int) -> int:
        # Tree approach
        # if n == 0 or n == 1 :
        #     return n
        # if n == 2 :
        #     return 1 

        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        # Dynamic Programming
        tribo_memo = {}

        def tribo(n) :
            # Use Memo
            if n in tribo_memo :
                return tribo_memo[n]
            
            # Base case :
            if n <= 1 :
                return n
            if n == 2 :
                return 1 

            # Dynamic Programming
            a = tribo(n-3)
            b = tribo(n-2)
            c = tribo(n-1)

            tribo_memo[n] = a + b + c

            return tribo_memo[n]
        
        return tribo(n)
