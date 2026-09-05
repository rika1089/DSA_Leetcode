class Solution:
    def possible(self, bloomDay: List[int], m: int, k: int, Day : int) -> int:
        cnt = 0
        noofB = 0
        if m * k > len(bloomDay) :
            return False

        for i in range(len(bloomDay)) :
            if bloomDay[i] <= Day :
                cnt += 1
                if cnt == k :
                    noofB += 1
                    cnt = 0
                    if noofB >= m :
                        return True
            else :
                cnt = 0
        return noofB >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high :
            mid = low + ( high - low ) // 2

            if self.possible(bloomDay, m, k, mid ) :
                ans = mid
                high = mid - 1
            else :
                low = mid + 1        
        return ans
