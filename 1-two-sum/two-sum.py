class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(len(nums)) :
            rem = target - nums[i]
            if rem in Map :
                return [i,Map[rem]]

            Map[nums[i]] = i
            
            
