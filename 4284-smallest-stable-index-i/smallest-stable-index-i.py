class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # TC = O(n^2)
        
        # n = len(nums)
        # for i in range(n) :
        #     left = nums[:i+1]   # O(i)
        #     right = nums[i:]    # O(n-i)

        #     maxele = max(left)   # O(i)
        #     minele = min(right)   # O(n-i)

        #     if maxele - minele <= k :
        #         return i
        
        # return -1


        # Optimise by using prefixmax & suffixmin for each index
        # Find for each index individually both
        # TC : O(n) + O(n) + O(n)

        n = len(nums)
        prefixmax = [0] * n
        suffixmin = [0] * n

        prefixmax[0] = nums[0]
        for i in range(1,n) :               # O(n)
            prefixmax[i] = max(prefixmax[i-1],nums[i])
        
        suffixmin[n-1] = nums[n-1]
        for i in range(n-2,-1,-1) :         # O(n)
            suffixmin[i] = min(suffixmin[i+1],nums[i])

        for i in range(n) :                 # O(n)
            if prefixmax[i] - suffixmin[i] <= k :
                return i
                                            # Total = O(3n) ~ O(n)
        return -1

       

