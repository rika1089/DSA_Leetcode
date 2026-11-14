class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n) :
            Sum = 0 
            for j in range(i, n) :
                Sum += nums[j]
                length = j-i+1
                if l <= length <= r and Sum > 0 :
                    ans = min(ans,Sum)
        return -1 if ans == float('inf') else ans