class Solution(object):
    def totalhrs(self,piles,k) :
        total_hrs = 0
        for i in range(len(piles)) :
            total_hrs += (piles[i]+k-1) // k
        return total_hrs


    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        low = 1
        high = max(piles) 
        ans = high
        while low <= high :
            mid = low + (high-low) // 2

            if self.totalhrs(piles,mid) <= h :
                ans = mid
                high = mid - 1
            
            else :
                low = mid + 1
        
        return ans


        