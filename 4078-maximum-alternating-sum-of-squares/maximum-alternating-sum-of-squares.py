class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # n = len(nums)                     # TC = O(nlogn + n)
        # nums.sort(key=abs)
        # Sum = 0
        # for i in range(n) :
        #     if i < n//2 :
        #         Sum -= nums[i]**2
        #     elif i >= n//2 :
        #         Sum += nums[i] ** 2
        # return Sum

        n = len(nums)                            # TC = O(n+n)
        sorted_nums = sorted(x*x for x in nums)
        # add the big squares, subtract the k smallest ones
        return sum(sorted_nums[n//2:])-sum(sorted_nums[:n//2])