class Solution:
    
    def fib(self, n: int,fibonacci_Map = None) -> int:
        if  fibonacci_Map is  None :
            fibonacci_Map = {}

        
        if n <= 1 :
            
            return n

        if n in fibonacci_Map :
            return fibonacci_Map[n]


        a = self.fib(n-1,fibonacci_Map )
        b = self.fib(n-2,fibonacci_Map )

        fibonacci_Map[n] = a+b

        return fibonacci_Map[n]


        