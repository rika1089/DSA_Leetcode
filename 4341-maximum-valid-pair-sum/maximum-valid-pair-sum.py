class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        lastmax = float('-inf')
        maxsum = float('-inf')
        for i in range(k,len(nums)) :
            lastmax = max(lastmax,nums[i-k])
            maxsum = max(maxsum,lastmax + nums[i])

        return maxsum