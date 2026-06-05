class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        n = len(nums)
        for i in range(n) :
            rem = target - nums[i]
            if rem in Map :
                return [Map[rem],i]

            Map[nums[i]] = i
        return []
        