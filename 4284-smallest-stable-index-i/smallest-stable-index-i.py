class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n) :
            left = nums[:i+1]
            right = nums[i:]

            maxele = max(left)
            minele = min(right)

            if maxele - minele <= k :
                return i
        
        return -1