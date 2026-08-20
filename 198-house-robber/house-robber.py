class Solution:
    def rob(self, nums: List[int]) -> int:
        house_memo = {}
        def houserobber(i,nums) :
            if i in house_memo :
                return house_memo[i]
            if i >= len(nums) :
                return 0
            
            rob = nums[i] + houserobber(i+2,nums)
            dontrob = houserobber(i+1,nums)

            house_memo[i] = max(rob , dontrob)

            return house_memo[i]

        return houserobber(0,nums)