class Solution:
    def eatbanana(self,piles:List[int],k:int)->int :
        hrs = 0
        for pile in piles :
            hrs += math.ceil(pile/k)
        return hrs
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = -1

        while low <= high :
            mid = low + ( high - low ) // 2
            if self.eatbanana(piles,mid) <= h :
                ans = mid
                high = mid - 1
            else :
                low = mid + 1
        return ans
