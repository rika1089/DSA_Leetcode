from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        Hash = defaultdict(int)
        Hash[0] = 1
        cnt = 0
        prefixSum = 0
        for i in range(n) :
            prefixSum += nums[i]

            remove = prefixSum - k
            if remove in Hash :
                cnt += Hash[remove]
            
            Hash[prefixSum] += 1
        
        return cnt
