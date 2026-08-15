class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xr = 0
        n = len(nums)
        flag = False
        for num in nums :
            xr ^= num
            if num != 0 and not flag :
                flag = True

        if not flag :
            return 0
        if xr == 0 :
            return n-1

        return n