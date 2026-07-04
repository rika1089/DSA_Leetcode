class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        midele = nums[n//2]
        cnt = 0
        for num in nums :
            if num == midele :
                cnt += 1

        return cnt == 1

        
        