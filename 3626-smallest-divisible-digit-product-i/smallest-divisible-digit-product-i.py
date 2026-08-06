class Solution:
    def prod(self, num:int) -> int :
        prod = 1
        for digit in str(num) :
            if digit == '0' :
                return 0
            prod *= int(digit)
        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n*t + 1):
            if self.prod(i) % t == 0:
                return i
        return -1
