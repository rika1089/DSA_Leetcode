from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Hash = defaultdict(int)
        Hash[0] = 1 # Store 0 PrefixSum also in the Hash (whihc is very very significant)
        cnt = 0

        prefixSum = 0

        for i in range(len(nums)) :
            prefixSum += nums[i]

            remove = prefixSum - k

            if remove in Hash :
                cnt += Hash[remove]

            Hash[prefixSum] += 1

        return cnt


        