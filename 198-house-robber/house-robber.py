class Solution:
    def rob(self, nums: List[int]) -> int:
        house_memo = {}
        def houserobber(i,nums) :
            # Use of memoization
            if i in house_memo :
                return house_memo[i]

            # Base case well written
            if i >= len(nums) :
                return 0
            
            # Dynamic Programming
            rob = nums[i] + houserobber(i+2,nums)
            dontrob = houserobber(i+1,nums)

            # Store the memoization
            house_memo[i] = max(rob , dontrob)

            return house_memo[i]

        return houserobber(0,nums)