class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        Sum = 0
        for digit in str(n).strip() :
            if digit != '0' :
                x += digit
                Sum += int(digit)

        return 0 if not x else int(x)*Sum
        