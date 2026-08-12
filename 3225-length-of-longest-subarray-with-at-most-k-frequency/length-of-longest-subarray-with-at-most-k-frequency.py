class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        Map = {}
        i = 0
        Len = 0

        for j in range(n):
            Map[nums[j]] = Map.get(nums[j], 0) + 1

            while Map[nums[j]] > k:
                Map[nums[i]] -= 1
                i += 1

            Len = max(Len, j - i + 1)

        return Len
