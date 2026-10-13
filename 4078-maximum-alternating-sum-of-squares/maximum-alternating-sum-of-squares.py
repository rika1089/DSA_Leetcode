class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(key=abs)
        Sum = 0
        for i in range(n) :
            if i < n//2 :
                Sum -= nums[i]**2
            elif i >= n//2 :
                Sum += nums[i] ** 2
        return Sum