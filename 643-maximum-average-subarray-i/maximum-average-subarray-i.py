from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        maxi = window_sum
        for i in range(k, len(nums)) :
            window_sum += nums[i] - nums[i-k]
            maxi = max(window_sum , maxi)

        return maxi/k

