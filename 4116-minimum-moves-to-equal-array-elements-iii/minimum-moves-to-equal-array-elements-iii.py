class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        return n*maxi - sum(nums)
        # return len(nums)*max(nums) - sum(nums)