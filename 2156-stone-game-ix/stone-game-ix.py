class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt0,cnt1,cnt2 = 0,0,0
        for stone in stones :
            if stone % 3 == 0 :
                cnt0 += 1
            elif stone % 3 == 1 :
                cnt1 += 1
            else :
                cnt2 += 1

        if cnt0 % 2 == 0 :
            return cnt1 > 0 and cnt2 > 0
        
        else :
            return abs(cnt1-cnt2) > 2
