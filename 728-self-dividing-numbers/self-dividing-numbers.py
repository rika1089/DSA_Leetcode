class Solution:
    def dividingbydigits(self, n : int)-> bool : 
        temp = n
        while temp > 0:
            d = temp % 10
            if d == 0 or n % d != 0:
                return False
            temp //= 10
        return True
            
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left,right+1) : 
            if self.dividingbydigits(num) :
                ans.append(num)

        return ans
