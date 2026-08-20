class Solution:
    
    def fib(self, n: int,fibonacci_Map = None) -> int:
        
        fibo_map = {}

        def fibonacci(n) :

            if n <= 1 :
                return n
            
            if n in fibo_map :
                return fibo_map[n]

            a = fibonacci(n-1)
            b = fibonacci(n-2)

            fibo_map[n] = a + b 
            return fibo_map[n]

        return fibonacci(n)