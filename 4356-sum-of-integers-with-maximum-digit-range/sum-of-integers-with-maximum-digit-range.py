class Solution:
    def getrange(self,num:int) -> int :
        minD = float('inf')
        maxD = float('-inf')

        for digit in list(str(num).strip()) :
            minD = min(minD,int(digit))
            maxD = max(maxD,int(digit))
            
        return maxD - minD


    def maxDigitRange(self, nums: list[int]) -> int:
        maxrange = 0
        candidates = []

        for num in nums :
            r = self.getrange(num)
            if r > maxrange :
                maxrange = r 
                candidates = [num]
            elif r==maxrange :
                candidates.append(num)
        return sum(candidates)