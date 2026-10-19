class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        left = right = 0
        for n in nums:
            if n <= target:
                right += 1
                if n < target:
                    left += 1
        return list(range(left, right))